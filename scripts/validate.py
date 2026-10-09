#!/usr/bin/env python3
"""Validate the public snapshot without executing learner solutions."""

import ast
import argparse
import json
from pathlib import Path
import re

from privacy import PUBLIC_DIRS, PUBLIC_FILES, PUBLIC_WORKFLOW, scan_public_tree

ROOT = Path(__file__).resolve().parents[1]


def validate(root):
    scanned = scan_public_tree(root)
    snapshot = json.loads((root / "data/progress.json").read_text(encoding="utf-8"))
    slugs = set()
    allowed = {"date", "number", "title", "leetcode_number", "slug", "difficulty", "topics", "status", "accepted_on", "profile_accepted", "problem_link", "question_path", "solution_path", "code_available", "complexity_available"}
    for record in snapshot["assignments"]:
        assert set(record) <= allowed, "Unexpected private metadata in public record"
        assert record["slug"] not in slugs, "Duplicate assignment"
        slugs.add(record["slug"])
        assert (root / record["question_path"]).is_file(), "Missing question brief"
        if record.get("solution_path"):
            assert record["status"] == "accepted", "Unconfirmed solution published"
            assert (root / record["solution_path"]).is_file(), "Missing solution notes"
        assert not record["code_available"] or record.get("solution_path"), "Code without archive"
    extra_allowed = {"date", "title", "leetcode_number", "slug", "difficulty", "topics", "status", "accepted_on", "profile_accepted", "problem_link", "code_available", "complexity_available"}
    for record in snapshot.get("additional_completions", []):
        assert set(record) <= extra_allowed, "Unexpected private metadata in additional completion"
        assert record["status"] == "accepted", "Unconfirmed additional completion published"
        assert record["slug"] not in slugs, "Duplicate completion slug"
        slugs.add(record["slug"])
        assert re.fullmatch(r"\d{4}-\d{2}-\d{2}", record["date"]), "Invalid additional completion date"
        assert re.fullmatch(r"\d{4}-\d{2}-\d{2}", record["accepted_on"]), "Invalid additional acceptance date"
        assert isinstance(record["leetcode_number"], int) and record["leetcode_number"] > 0, "Invalid additional LeetCode number"
        assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", record["slug"]), "Unsafe additional slug"
        assert record["problem_link"] == "https://leetcode.com/problems/" + record["slug"] + "/", "Unexpected additional problem link"
        assert record["code_available"] is False and record["complexity_available"] is False, "Unarchived additional solution claims code or analysis"
    paths = [path for path in root.rglob("*") if path.is_file() and
             (path.relative_to(root).parts[0] in PUBLIC_DIRS | PUBLIC_FILES or path.relative_to(root).as_posix() == PUBLIC_WORKFLOW) and
             "__pycache__" not in path.parts]
    for path in (path for path in paths if path.suffix == ".py"):
        ast.parse(path.read_text(encoding="utf-8"), filename=path.name)
    for path in (path for path in paths if path.suffix == ".md"):
        text = path.read_text(encoding="utf-8")
        assert "/Users/" not in text and "/var/folders/" not in text, "Local path in public Markdown"
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            if "://" not in target and not target.startswith("#"):
                assert (path.parent / target.split("#", 1)[0]).exists(), "Broken local link: " + target
    print(f"Validated {len(slugs)} assignments, Python syntax, Markdown links, and privacy patterns across {scanned} public files.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    validate(parser.parse_args().root)
