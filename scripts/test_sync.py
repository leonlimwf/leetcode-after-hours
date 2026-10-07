"""Test acceptance gating, deterministic exports, and midnight preservation."""

import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import xml.etree.ElementTree as ET
import zipfile

import sync


class ExportTests(unittest.TestCase):
    def test_acceptance_gating_idempotence_and_midnight(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            public = root / "public"
            public.mkdir()
            ledger = root / "private.json"
            assignments = [
                {"date": "2026-10-01", "number": 1, "title": "First", "leetcode_number": 1, "slug": "first", "difficulty": "Easy", "topics": ["Array"], "status": "accepted", "accepted_on": "2026-10-01"},
                {"date": "2026-10-02", "number": 2, "title": "Second", "leetcode_number": 2, "slug": "second", "difficulty": "Easy", "topics": ["Array"], "status": "in_progress", "profile_observed_status": "Accepted", "private_note": "DO_NOT_PUBLISH"},
            ]
            ledger.write_text(json.dumps({"owner": "example", "timezone": "Asia/Singapore", "started_on": "2026-10-01", "completion_rule": "Explicit confirmation", "assigned": assignments}))
            journal = root / "private.docx"
            lines = []
            for number, title in [(1, "First"), (2, "Second")]:
                lines.extend([f"{number:02}  {title}", "Problem Statement", "A practice problem.", "Input and Output", "Input: nums", "Examples", "Constraints", "n >= 1", "Your Work", "First Instinct  |  What approach would you try first, and why?", " class Solution:", "    def solve(self):", "        return 1", "Complexity Analysis", "Time: O(1).", "Space: O(1).", "Completion Check"])
            document = ET.Element(sync.W + "document")
            body = ET.SubElement(document, sync.W + "body")
            for text in lines:
                p = ET.SubElement(body, sync.W + "p")
                r = ET.SubElement(p, sync.W + "r")
                ET.SubElement(r, sync.W + "t").text = text
            with zipfile.ZipFile(journal, "w") as archive:
                archive.writestr("word/document.xml", ET.tostring(document))
            with patch.object(sync, "ROOT", public), contextlib.redirect_stdout(io.StringIO()):
                sync.export(ledger, journal, "check")
                snapshot = json.loads((public / "data/progress.json").read_text())
                self.assertTrue(snapshot["assignments"][0]["code_available"])
                self.assertFalse(snapshot["assignments"][1]["code_available"])
                self.assertTrue(snapshot["assignments"][1]["profile_accepted"])
                self.assertFalse((public / "solutions/0002-second").exists())
                all_files = {p.relative_to(public): p.read_bytes() for p in public.rglob("*") if p.is_file()}
                self.assertNotIn(b"DO_NOT_PUBLISH", b"".join(all_files.values()))
                sync.export(ledger, journal, "check")
                self.assertEqual(all_files, {p.relative_to(public): p.read_bytes() for p in public.rglob("*") if p.is_file()})
                code_path = public / "solutions/0001-first/solution.py"
                code_path.write_text("# Existing published snapshot\n")
                sync.export(ledger, journal, "midnight")
                self.assertEqual(code_path.read_text(), "# Existing published snapshot\n")


if __name__ == "__main__":
    unittest.main()
