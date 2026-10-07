"""Fail publishing when likely credentials or private material are detected."""

from pathlib import Path
import re

PUBLIC_FILES = {"README.md", "QUESTIONS.md", "PROGRESS.md", ".gitignore"}
PUBLIC_DIRS = {"data", "questions", "solutions", "scripts", "docs"}
PUBLIC_WORKFLOW = ".github/workflows/validate.yml"
RULES = {
    "private key": r"-----BEGIN (?:RSA |EC |OPENSSH |DSA |ENCRYPTED )?PRIVATE KEY-----",
    "GitHub credential": r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b",
    "OpenAI credential": r"\bsk-(?:proj-|svcacct-)?[A-Za-z0-9_-]{24,}\b",
    "AWS access key": r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b",
    "Google API credential": r"\bAIza[A-Za-z0-9_-]{30,}\b",
    "Slack credential": r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b",
    "credential in URL": r"https?://[^\s/@:]+:[^\s/@]+@",
    "local home path": r"(?:/Users/|/home/)[A-Za-z0-9._-]+/",
    "local attachment path": r"/(?:private/)?var/folders/[A-Za-z0-9_/.-]+",
    "email address": r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
    "credential assignment": r'''(?im)\b(?:api[_-]?key|access[_-]?token|secret[_-]?key|password|LEETCODE_SESSION|csrftoken)\b\s*[:=]\s*["'][^"'\s]{8,}["']''',
    "JWT": r"\beyJ[A-Za-z0-9_-]{15,}\.[A-Za-z0-9_-]{15,}\.[A-Za-z0-9_-]{15,}\b",
}


def scan_text(text):
    # Report only categories; never print or include the matching secret.
    return [name for name, pattern in RULES.items() if re.search(pattern, text)]


def scan_public_tree(root):
    issues = []
    count = 0
    for relative in (".github", ".github/workflows"):
        if (root / relative).is_symlink():
            raise ValueError("Privacy check blocked publishing: " + relative + " (symlink)")
    for path in root.rglob("*"):
        relative = path.relative_to(root)
        workflow = relative.as_posix() == PUBLIC_WORKFLOW
        if not relative.parts or (relative.parts[0] not in PUBLIC_DIRS | PUBLIC_FILES and not workflow):
            continue
        if "__pycache__" in relative.parts:
            continue
        if path.is_symlink():
            issues.append((relative.as_posix(), "symlink"))
            continue
        if not path.is_file():
            continue
        if path.name != ".gitignore" and path.suffix not in {".md", ".py", ".json"} and not workflow:
            issues.append((relative.as_posix(), "unexpected file type"))
            continue
        if path.name.startswith(".env") or path.name == "leetcode_progress.json":
            issues.append((relative.as_posix(), "private file name"))
            continue
        count += 1
        for category in scan_text(path.read_text(encoding="utf-8")):
            issues.append((relative.as_posix(), category))
    if issues:
        safe_report = "; ".join(path + " (" + category + ")" for path, category in issues)
        raise ValueError("Privacy check blocked publishing: " + safe_report)
    return count
