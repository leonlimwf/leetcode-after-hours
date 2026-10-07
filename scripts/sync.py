#!/usr/bin/env python3
"""Export a public practice snapshot from a private ledger and Word journal."""

import argparse
import ast
from collections import Counter
import json
from pathlib import Path
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[1]
NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
W = "{" + NS["w"] + "}"
EXPECTED_REMOTE = "https://github.com/leonlimwf/leetcode-after-hours.git"
PUBLIC_PATHS = ["README.md", "QUESTIONS.md", "PROGRESS.md", "data", "questions", "solutions", "scripts", "docs", ".gitignore"]


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
            if match and int(match[1]) in headings and match[2] == headings[int(match[1])]["title"]:
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
    index = next((i for i, text in enumerate(lines) if text.strip() == start or text.strip().startswith(start + "  |")), None)
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
    # Word contains an incidental space before some top-level class headings.
    code_lines = [line.lstrip() if re.match(r"^ (?:class|def)\s", line) else line for line in code_lines]
    code = "\n".join(code_lines).rstrip() + "\n"
    ast.parse(code)
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


def export(ledger_path, journal_path, phase, since=None):
    ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
    assignments = ledger["assigned"]
    entries = journal_entries(journal_path, assignments)
    if since:
        assignments = [assignment for assignment in assignments if assignment["date"] >= since]
    records = []
    slugs = set()
    for assignment in assignments:
        slug = assignment["slug"]
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
        solution_dir = ROOT / "solutions" / (str(assignment["leetcode_number"]).zfill(4) + "-" + slug)
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
            record["solution_path"] = solution_dir.relative_to(ROOT).as_posix() + "/README.md"
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
        write(ROOT / record["question_path"], brief)
        records.append(record)
    snapshot = {"version": 1, "owner": ledger["owner"], "timezone": ledger["timezone"], "started_on": ledger["started_on"], "completion_rule": ledger["completion_rule"], "assignments": records}
    write(ROOT / "data/progress.json", json.dumps(snapshot, indent=2, ensure_ascii=False) + "\n")
    questions = "# Daily Questions\n\nFresh assignments selected by ChatGPT. All dates use Asia/Singapore.\n\n| Assigned | # | Problem | Difficulty | Topics | Status |\n| --- | --- | --- | --- | --- | --- |\n"
    for record in reversed(records):
        questions += f"| {record['date']} | {record['leetcode_number']} | [{record['title']}]({record['question_path']}) | {record['difficulty']} | {', '.join(record['topics'])} | {label(record)} |\n"
    write(ROOT / "QUESTIONS.md", questions)
    completed = [r for r in records if r["status"] == "accepted"]
    counts = Counter(r["difficulty"] for r in completed)
    progress = f"# Confirmed Completions\n\n**{len(completed)} confirmed Accepted** · {counts['Easy']} Easy · {counts['Medium']} Medium · {counts['Hard']} Hard\n\nThese dates come from the existing tracking ledger. Profile-observed acceptance awaits learner confirmation. Archived code is the journal snapshot, not a fetched copy of a private LeetCode submission.\n\n| Accepted | # | Problem | Difficulty | Code / analysis |\n| --- | --- | --- | --- | --- |\n"
    for record in reversed(completed):
        archive = f"[Journal snapshot]({record['solution_path']})" if record.get("solution_path") else "Not published yet"
        progress += f"| {record.get('accepted_on', 'Not recorded')} | {record['leetcode_number']} | [{record['title']}]({record['problem_link']}) | {record['difficulty']} | {archive} |\n"
    progress += "\n## Awaiting completion or confirmation\n\n"
    for record in records:
        if record["status"] != "accepted":
            progress += f"- [{record['title']}]({record['question_path']}) — {label(record)}\n"
    write(ROOT / "PROGRESS.md", progress)
    print(f"Exported {len(records)} assignments and {len(completed)} confirmed completions.")


def git(*args):
    result = subprocess.run(["git", "-C", str(ROOT), *args], check=True, capture_output=True, text=True)
    return result.stdout.strip()


def prepare_publish():
    if Path(git("rev-parse", "--show-toplevel")).resolve() != ROOT:
        raise ValueError("Expected a dedicated repository checkout.")
    if git("remote", "get-url", "origin") not in {EXPECTED_REMOTE, "git@github.com:leonlimwf/leetcode-after-hours.git"}:
        raise ValueError("Unexpected origin; refusing to publish.")
    if git("branch", "--show-current") != "main":
        raise ValueError("Publishing is supported only on main.")
    if git("status", "--porcelain", "--untracked-files=no"):
        raise ValueError("Tracked changes are present. Review or commit them before publishing.")
    git("pull", "--ff-only", "origin", "main")


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
    lock = ROOT / ".sync.lock"
    try:
        lock.mkdir()
    except FileExistsError:
        parser.exit(1, "Another sync is active. If a previous run crashed, inspect it before removing .sync.lock.\n")
    try:
        if args.publish:
            prepare_publish()
        export(args.ledger, args.journal, args.phase, args.since)
        subprocess.run([sys.executable, str(ROOT / "scripts/validate.py")], check=True)
        if args.publish:
            git("add", "--", *PUBLIC_PATHS)
            if git("diff", "--cached", "--name-only"):
                records = json.loads((ROOT / "data/progress.json").read_text(encoding="utf-8"))["assignments"]
                date = records[-1]["date"] if records else "setup"
                git("commit", "-m", f"practice: {args.phase} sync for {date}")
            # Also retries a commit whose earlier push failed, without duplicating it.
            git("push", "origin", "main")
            print("Published to https://github.com/leonlimwf/leetcode-after-hours")
    finally:
        lock.rmdir()


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, KeyError, subprocess.CalledProcessError) as error:
        # Keep private input paths and remote authentication output out of logs.
        print("Sync failed (" + type(error).__name__ + "). Review local inputs, Git status, and authentication; nothing was force-pushed.", file=sys.stderr)
        raise SystemExit(1)
