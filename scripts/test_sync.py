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
from privacy import scan_public_tree


class ExportTests(unittest.TestCase):
    def test_remote_fast_forward_pending_push_and_divergence(self):
        for history, expected_merge in [("0 2", True), ("2 0", False), ("0 0", False)]:
            with self.subTest(history=history), patch.object(sync, "git") as git:
                git.side_effect = [str(sync.ROOT), sync.EXPECTED_REMOTE, "main", "", "", history] + ([""] if expected_merge else [])
                sync.prepare_publish()
                self.assertEqual(any(call.args == ("merge", "--ff-only", "origin/main") for call in git.call_args_list), expected_merge)
        with patch.object(sync, "git", side_effect=[str(sync.ROOT), sync.EXPECTED_REMOTE, "main", "", "", "1 1"]):
            with self.assertRaises(ValueError):
                sync.prepare_publish()

    def test_lock_released_on_failure_and_blocks_overlap(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with sync.sync_lock(root):
                with self.assertRaises(ValueError):
                    with sync.sync_lock(root):
                        pass
            with self.assertRaises(RuntimeError):
                with sync.sync_lock(root):
                    raise RuntimeError("Simulated failure")
            with sync.sync_lock(root):
                pass

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
            filtered = root / "filtered"
            filtered.mkdir()
            with patch.object(sync, "ROOT", filtered), contextlib.redirect_stdout(io.StringIO()):
                sync.export(ledger, journal, "check", since="2026-10-02")
                snapshot = json.loads((filtered / "data/progress.json").read_text())
                self.assertEqual([record["slug"] for record in snapshot["assignments"]], ["second"])
                self.assertFalse((filtered / "solutions/0001-first").exists())
                self.assertFalse((filtered / "questions/2026-10-01-first.md").exists())
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
                with sync.sync_lock(public) as state, patch.object(sync, "export", wraps=sync.export) as exporter:
                    sync.export_checked(ledger, journal, "check", None, state)
                    private = json.loads(ledger.read_text())
                    private["notes"] = "Non-exported private metadata changed"
                    ledger.write_text(json.dumps(private))
                    sync.export_checked(ledger, journal, "check", None, state)
                    self.assertEqual(exporter.call_count, 1)
                    # A damaged public file invalidates the cache and is repaired.
                    code_path.write_text("# Altered snapshot\n")
                    sync.export_checked(ledger, journal, "check", None, state)
                    self.assertEqual(exporter.call_count, 2)
                    self.assertIn("return 1", code_path.read_text())
                    before = {p.relative_to(public): p.read_bytes() for p in sync.public_files(public)}
                    private = json.loads(ledger.read_text())
                    private["assigned"][0]["title"] = "Changed title"
                    ledger.write_text(json.dumps(private))
                    with self.assertRaises(ValueError):
                        sync.export_checked(ledger, journal, "check", None, state)
                    self.assertEqual(before, {p.relative_to(public): p.read_bytes() for p in sync.public_files(public)})
                self.assertGreater(scan_public_tree(public), 0)


if __name__ == "__main__":
    unittest.main()
