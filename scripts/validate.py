#!/usr/bin/env python3
"""Validate the public snapshot without executing learner solutions."""

import ast
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def main():
    snapshot = json.loads((ROOT / "data/progress.json").read_text(encoding="utf-8"))
    slugs = set()
    allowed = {"date", "number", "title", "leetcode_number", "slug", "difficulty", "topics", "status", "accepted_on", "profile_accepted", "problem_link", "question_path", "solution_path", "code_available", "complexity_available"}
    for record in snapshot["assignments"]:
        assert set(record) <= allowed, "Unexpected private metadata in public record"
        assert record["slug"] not in slugs, "Duplicate assignment"
        slugs.add(record["slug"])
        assert (ROOT / record["question_path"]).is_file(), "Missing question brief"
        if record.get("solution_path"):
            assert record["status"] == "accepted", "Unconfirmed solution published"
            assert (ROOT / record["solution_path"]).is_file(), "Missing solution notes"
        assert not record["code_available"] or record.get("solution_path"), "Code without archive"
    for path in ROOT.rglob("*.py"):
        ast.parse(path.read_text(encoding="utf-8"), filename=path.name)
    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        assert "/Users/" not in text and "/var/folders/" not in text, "Local path in public Markdown"
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            if "://" not in target and not target.startswith("#"):
                assert (path.parent / target.split("#", 1)[0]).exists(), "Broken local link: " + target
    print(f"Validated {len(slugs)} assignments, Python syntax, and Markdown links.")


if __name__ == "__main__":
    main()
