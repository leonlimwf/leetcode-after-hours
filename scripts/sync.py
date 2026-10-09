#!/usr/bin/env python3
"""Export a public practice snapshot from a private ledger and Word journal."""

import argparse
import ast
from collections import Counter
from contextlib import contextmanager
import fcntl
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[1]
NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
W = "{" + NS["w"] + "}"
EXPECTED_REMOTE = "https://github.com/leonlimwf/leetcode-after-hours.git"
PUBLIC_PATHS = ["README.md", "QUESTIONS.md", "PROGRESS.md", "data", "questions", "solutions", "scripts", "docs", ".gitignore", ".github/workflows/validate.yml"]


def paragraph_text(element):
    parts = []
    for node in element.iter():
        if node.tag == W + "t":
            parts.append(node.text or "")
        elif node.tag == W + "tab":
            parts.append("\t")
        elif node.tag in {W + "br", W + "cr"}:
            parts.append("\n")
    return "".join(parts)


def journal_entries(path, assignments):
    with zipfile.ZipFile(path) as docx:
        document = ET.fromstring(docx.read("word/document.xml"))
    entries = {}
    current = None
    headings = {int(a["number"]): a for a in assignments}
    for element in document.find("w:body", NS):
        if element.tag == W + "p":
            text = paragraph_text(element)
            match = re.fullmatch(r"(\d+)\s+(.+)", text.strip())
            if match and int(match[1]) in headings and " ".join(match[2].split()) == " ".join(headings[int(match[1])]["title"].split()):
                current = headings[int(match[1])]["slug"]
                if current in entries:
                    raise ValueError("Duplicate journal entry: " + current)
                entries[current] = []
            elif text.strip() == "Completion Tracker":
                current = None
            elif current:
                entries[current].append(text)
        elif element.tag == W + "tbl" and current:
            for index, row in enumerate(element.findall("w:tr", NS)):
                cells = ["\n".join(paragraph_text(p) for p in cell.findall(".//w:p", NS)) for cell in row.findall("w:tc", NS)]
                cells = [cell.replace("|", "\\|").replace("\n", "<br>") for cell in cells]
                entries[current].append("| " + " | ".join(cells) + " |")
                if index == 0:
                    entries[current].append("| " + " | ".join("---" for _ in cells) + " |")
    return entries


def section(lines, start, ends):
    index = next((i for i, text in enumerate(lines) if text.strip() == start or re.match(re.escape(start) + r"\s*\|", text.strip())), None)
    if index is None:
        return []
    stop = next((i for i in range(index + 1, len(lines)) if lines[i].strip() in ends), len(lines))
    return lines[index + 1:stop]


def solution_code(lines):
    work = section(lines, "First Instinct", {"Complexity Analysis", "Completion Check"})
    index = next((i for i, text in enumerate(work) if re.match(r"\s*(?:#\s*Definition|class\s+Solution\b|def\s+\w+|from\s+\w+\s+import|import\s+\w+)", text)), None)
    if index is None:
        return None
    code_lines = work[index:]
    # Explicit boundaries only: never trim broken Python until it parses.
    stop = next((i for i, text in enumerate(code_lines) if text.strip() == "```" or re.match(r"^(?:Notes|My approach|Reflection):", text)), len(code_lines))
    if any(re.match(r"\s*(?:class\s+Solution\b|def\s+\w+|```python)", text) for text in code_lines[stop + 1:]):
        raise ValueError("Multiple solution blocks; explicitly select the submitted code.")
    code_lines = code_lines[:stop]
    # Word contains an incidental space before some top-level class headings.
    code_lines = [line.lstrip() if re.match(r"^ (?:class|def)\s", line) else line for line in code_lines]
    code = "\n".join(code_lines).rstrip() + "\n"
    tree = ast.parse(code)
    if sum(isinstance(node, ast.ClassDef) and node.name == "Solution" for node in tree.body) > 1:
        raise ValueError("Multiple solution versions; explicitly select the submitted code.")
    return code


def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists() or path.read_text(encoding="utf-8") != content:
        path.write_text(content, encoding="utf-8")


def label(record):
    if record["status"] == "accepted":
        return "Accepted"
    if record.get("profile_accepted"):
        return "Profile Accepted · pending confirmation"
    return {"assigned": "Assigned", "in_progress": "In Progress", "missed": "Missed", "skipped": "Skipped"}.get(record["status"], record["status"])


def export(ledger_path, journal_path, phase, since=None, output_root=None):
    output_root = output_root or ROOT
    ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
    assignments = ledger["assigned"]
    entries = journal_entries(journal_path, assignments)
    assignment_slugs = {assignment["slug"] for assignment in assignments}
    additional = []
    extra_keys = ("date", "leetcode_number", "title", "slug", "difficulty", "topics", "status", "accepted_on")
    for item in ledger.get("additional_completions", []):
        if item.get("status") != "accepted":
            raise ValueError("Additional completion is not user-confirmed Accepted: " + str(item.get("slug", "unknown")))
        if item.get("slug") in assignment_slugs:
            raise ValueError("Additional completion duplicates a daily assignment: " + item["slug"])
        if since and item["date"] < since:
            continue
        record = {key: item[key] for key in extra_keys}
        record["profile_accepted"] = item.get("profile_observed_status") == "Accepted"
        record["problem_link"] = "https://leetcode.com/problems/" + item["slug"] + "/"
        record["code_available"] = False
        record["complexity_available"] = False
        additional.append(record)
    if since:
        assignments = [assignment for assignment in assignments if assignment["date"] >= since]
    records = []
    slugs = set()
    for assignment in assignments:
        slug = assignment["slug"]
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", assignment["date"]):
            raise ValueError("Invalid assignment date.")
        if not isinstance(assignment["leetcode_number"], int) or assignment["leetcode_number"] <= 0:
            raise ValueError("Invalid LeetCode problem number.")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug) or slug in slugs:
            raise ValueError("Unsafe or duplicate slug: " + slug)
        slugs.add(slug)
        lines = entries.get(slug)
        if lines is None:
            raise ValueError("Assignment missing from journal: " + slug)
        record = {key: assignment[key] for key in ("date", "number", "title", "leetcode_number", "slug", "difficulty", "topics", "status")}
        if assignment.get("accepted_on"):
            record["accepted_on"] = assignment["accepted_on"]
        record["profile_accepted"] = assignment.get("profile_observed_status") == "Accepted"
        record["problem_link"] = "https://leetcode.com/problems/" + slug + "/"
        record["question_path"] = "questions/" + assignment["date"] + "-" + slug + ".md"
        solution_dir = output_root / "solutions" / (str(assignment["leetcode_number"]).zfill(4) + "-" + slug)
        code = None
        syntax_issue = False
        # Midnight publishes briefs, but does not refresh learner code snapshots.
        if assignment["status"] == "accepted" and phase != "midnight":
            try:
                code = solution_code(lines)
            except SyntaxError:
                syntax_issue = True
                print("Skipped code with invalid Python syntax: " + slug, file=sys.stderr)
            if code:
                write(solution_dir / "solution.py", code)
            elif (solution_dir / "solution.py").exists():
                raise ValueError("Previously published code is missing or invalid in the journal: " + slug)
            complexity = section(lines, "Complexity Analysis", {"Completion Check"})
            complexity = "\n\n".join(text for text in complexity if text.strip())
            record["complexity_available"] = bool(complexity)
            note = "Python could not be exported because the journal code has a syntax error." if syntax_issue else "No executable code is recorded in the journal yet."
            solution_readme = f"# {assignment['leetcode_number']}. {assignment['title']}\n\n{assignment['difficulty']} · {' / '.join(assignment['topics'])}\n\n[Original problem]({record['problem_link']}) · Confirmed Accepted: {assignment.get('accepted_on', 'date not recorded')}\n\n"
            solution_readme += "[Python solution](solution.py)\n\nCode is copied from my practice journal; it may include ChatGPT assistance. LeetCode supplies the node types and submission environment.\n\n" if code else note + "\n\n"
            solution_readme += "## Complexity Analysis\n\n" + (complexity or "Analysis has not been recorded in the journal yet; no bounds are inferred by the publisher.") + "\n"
            write(solution_dir / "README.md", solution_readme)
        if assignment["status"] == "accepted" and (solution_dir / "README.md").exists():
            record["solution_path"] = solution_dir.relative_to(output_root).as_posix() + "/README.md"
            record["code_available"] = (solution_dir / "solution.py").exists()
            if "complexity_available" not in record:
                record["complexity_available"] = "Analysis has not been recorded" not in (solution_dir / "README.md").read_text(encoding="utf-8")
        else:
            record["code_available"] = False
            record["complexity_available"] = False
        brief = f"# {assignment['leetcode_number']}. {assignment['title']}\n\nAssigned: **{assignment['date']}** · **{assignment['difficulty']}**\n\nTopics: {' / '.join(assignment['topics'])}\n\n[Open on LeetCode]({record['problem_link']})\n\nStatus: **{label(record)}**\n\n"
        for heading, ends in [("Problem Statement", {"Input and Output"}), ("Input and Output", {"Examples"}), ("Examples", {"Constraints"}), ("Constraints", {"Your Work"})]:
            content = section(lines, heading, ends)
            if any(text.strip() for text in content):
                brief += "## " + heading + "\n\n"
                for index, text in enumerate(content):
                    if text.strip():
                        brief += text + ("\n" if text.startswith("| ") else "\n\n")
                brief += "\n"
        brief += "## First Instinct\n\nWhat approach would you try first, and why?\n\nTry it before reading a solution. Write your approach and code in your private journal.\n"
        if record.get("solution_path"):
            brief += "\n[Archived solution and complexity](../" + record["solution_path"] + ")\n"
        write(output_root / record["question_path"], brief)
        records.append(record)
    snapshot = {"version": 1, "owner": ledger["owner"], "timezone": ledger["timezone"], "started_on": ledger["started_on"], "completion_rule": ledger["completion_rule"], "assignments": records, "additional_completions": additional}
    write(output_root / "data/progress.json", json.dumps(snapshot, indent=2, ensure_ascii=False) + "\n")
    questions = "# Daily Questions\n\nFresh assignments selected by ChatGPT. All dates use Asia/Singapore.\n\n| Assigned | # | Problem | Difficulty | Topics | Status |\n| --- | --- | --- | --- | --- | --- |\n"
    for record in reversed(records):
        questions += f"| {record['date']} | {record['leetcode_number']} | [{record['title']}]({record['question_path']}) | {record['difficulty']} | {', '.join(record['topics'])} | {label(record)} |\n"
    write(output_root / "QUESTIONS.md", questions)
    completed = [r for r in records if r["status"] == "accepted"]
    counts = Counter(r["difficulty"] for r in completed + additional)
    total_completed = len(completed) + len(additional)
    progress = f"# Confirmed Completions\n\n**{total_completed} confirmed Accepted** · {counts['Easy']} Easy · {counts['Medium']} Medium · {counts['Hard']} Hard\n\nThis includes {len(completed)} daily assignment completions and {len(additional)} additional accepted problem(s). Profile-only acceptance still awaits learner confirmation. Archived code is copied from the private journal; no private LeetCode submission source is fetched.\n\n| Accepted | # | Problem | Difficulty | Code / analysis |\n| --- | --- | --- | --- | --- |\n"
    for record in reversed(completed):
        archive = f"[Journal snapshot]({record['solution_path']})" if record.get("solution_path") else "Not published yet"
        progress += f"| {record.get('accepted_on', 'Not recorded')} | {record['leetcode_number']} | [{record['title']}]({record['problem_link']}) | {record['difficulty']} | {archive} |\n"
    if additional:
        progress += "\n## Additional accepted problems\n\nThese are user-confirmed completions outside the daily assignment pages. No code or complexity is published unless it is present in the journal.\n\n| Accepted | # | Problem | Difficulty | Code / analysis |\n| --- | --- | --- | --- | --- |\n"
        for record in reversed(additional):
            progress += f"| {record['accepted_on']} | {record['leetcode_number']} | [{record['title']}]({record['problem_link']}) | {record['difficulty']} | Not in journal |\n"
    progress += "\n## Awaiting completion or confirmation\n\n"
    for record in records:
        if record["status"] != "accepted":
            progress += f"- [{record['title']}]({record['question_path']}) — {label(record)}\n"
    write(output_root / "PROGRESS.md", progress)
    print(f"Exported {len(records)} assignments and {len(completed)} confirmed completions.")


def git(*args):
    result = subprocess.run(["git", "-C", str(ROOT), *args], check=True, capture_output=True, text=True, timeout=45)
    return result.stdout.strip()


def prepare_publish():
    if Path(git("rev-parse", "--show-toplevel")).resolve() != ROOT:
        raise ValueError("Expected a dedicated repository checkout.")
    if git("remote", "get-url", "origin") != EXPECTED_REMOTE:
        raise ValueError("Unexpected origin; refusing to publish.")
    if git("branch", "--show-current") != "main":
        raise ValueError("Publishing is supported only on main.")
    if git("status", "--porcelain", "--untracked-files=no"):
        raise ValueError("Tracked changes are present. Review or commit them before publishing.")
    git("fetch", "origin", "main")
    # Supports a prior local commit whose push failed, without needless merges.
    ahead, behind = map(int, git("rev-list", "--left-right", "--count", "HEAD...origin/main").split())
    if ahead and behind:
        raise ValueError("Local and remote history diverged; manual review required.")
    if behind:
        git("merge", "--ff-only", "origin/main")


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


@contextmanager
def sync_lock(root):
    # OS releases flock on normal exit, exceptions, or process termination.
    directory = root / ".sync.lock"
    if directory.is_symlink() or (directory / "publish.lock").is_symlink():
        raise ValueError("Expected a regular local sync lock.")
    directory.mkdir(exist_ok=True)
    with (directory / "publish.lock").open("a") as handle:
        try:
            fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise ValueError("Another sync is active.") from None
        try:
            yield directory
        finally:
            fcntl.flock(handle, fcntl.LOCK_UN)


def public_files(root):
    for relative in PUBLIC_PATHS:
        path = root / relative
        if path.is_file():
            yield path
        elif path.is_dir():
            yield from (p for p in sorted(path.rglob("*")) if p.is_file() and "__pycache__" not in p.parts)


def tree_hash(root):
    digest = hashlib.sha256()
    for path in public_files(root):
        digest.update(path.relative_to(root).as_posix().encode())
        digest.update(bytes.fromhex(sha256(path)))
    return digest.hexdigest()


def public_ledger_hash(path, since):
    ledger = json.loads(path.read_text())
    keys = ("date", "number", "title", "leetcode_number", "slug", "difficulty", "topics", "status", "accepted_on", "profile_observed_status")
    visible = {key: ledger[key] for key in ("owner", "timezone", "started_on", "completion_rule")}
    visible["assigned"] = [{key: a[key] for key in keys if key in a}
                           for a in ledger["assigned"] if not since or a["date"] >= since]
    extra_keys = ("date", "leetcode_number", "title", "slug", "difficulty", "topics", "status", "accepted_on", "profile_observed_status")
    visible["additional_completions"] = [{key: item[key] for key in extra_keys if key in item}
                                         for item in ledger.get("additional_completions", [])
                                         if not since or item["date"] >= since]
    return hashlib.sha256(json.dumps(visible, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def export_checked(ledger, journal, phase, since, state_dir):
    from validate import validate
    from privacy import scan_public_tree

    scan_public_tree(ROOT)  # Privacy checks run even on a cache hit.
    input_hashes = {"ledger": sha256(ledger), "journal": sha256(journal)}
    # Private observation timestamps/notes don't affect the public export.
    source = {"ledger": public_ledger_hash(ledger, since), "journal": input_hashes["journal"], "phase": phase, "since": since}
    source["exporter"] = sha256(Path(__file__))
    state_path = state_dir / "state.json"
    try:
        previous = json.loads(state_path.read_text())
    except (OSError, ValueError):
        previous = {}
    if previous.get("source") == source and previous.get("public_sha256") == tree_hash(ROOT):
        validate(ROOT)
        print("Source and public snapshot unchanged; skipped archive regeneration.")
        return
    # Generate and validate off-checkout. A failed export leaves existing files intact.
    with tempfile.TemporaryDirectory(prefix="leetcode-export-") as directory:
        candidate = Path(directory)
        for path in public_files(ROOT):
            target = candidate / path.relative_to(ROOT)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, target)
        export(ledger, journal, phase, since, output_root=candidate)
        validate(candidate)
        if input_hashes["ledger"] != sha256(ledger) or input_hashes["journal"] != sha256(journal):
            raise ValueError("Private inputs changed during export; retry with a stable snapshot.")
        for path in public_files(candidate):
            target = ROOT / path.relative_to(candidate)
            if not target.exists() or target.read_bytes() != path.read_bytes():
                target.parent.mkdir(parents=True, exist_ok=True)
                temporary = state_dir / "promote" / path.relative_to(candidate)
                temporary.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(path, temporary)
                temporary.replace(target)
    write(state_path, json.dumps({"source": source, "public_sha256": tree_hash(ROOT)}, sort_keys=True) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ledger", type=Path, required=True)
    parser.add_argument("--journal", type=Path, required=True)
    parser.add_argument("--phase", choices=["bootstrap", "midnight", "check"], required=True)
    parser.add_argument("--since", help="Publish only assignments on or after this YYYY-MM-DD date")
    parser.add_argument("--publish", action="store_true")
    args = parser.parse_args()
    if args.since and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", args.since):
        parser.error("--since must be YYYY-MM-DD")
    with sync_lock(ROOT) as state_dir:
        if args.publish:
            prepare_publish()
        export_checked(args.ledger, args.journal, args.phase, args.since, state_dir)
        if args.publish:
            git("add", "--", *(path for path in PUBLIC_PATHS if (ROOT / path).exists()))
            if git("diff", "--cached", "--name-only"):
                records = json.loads((ROOT / "data/progress.json").read_text(encoding="utf-8"))["assignments"]
                date = records[-1]["date"] if records else "setup"
                git("commit", "-m", f"practice: {args.phase} sync for {date}")
            # Also retries a commit whose earlier push failed, without duplicating it.
            if git("rev-list", "--count", "origin/main..HEAD") != "0":
                git("push", "origin", "main")
                print("Published to https://github.com/leonlimwf/leetcode-after-hours")
            else:
                print("GitHub already up to date; no commit or push needed.")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, KeyError, subprocess.CalledProcessError, subprocess.TimeoutExpired) as error:
        # Keep private input paths and remote authentication output out of logs.
        print("Sync failed (" + type(error).__name__ + "). Review local inputs, Git status, and authentication; nothing was force-pushed.", file=sys.stderr)
        raise SystemExit(1)
