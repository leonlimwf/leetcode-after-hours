"""Regression tests for timezone jitter, solved history, selection and code provenance."""

import json
from pathlib import Path
import tempfile
from unittest.mock import patch, MagicMock
import unittest

import sync
import workflow


class WorkflowTests(unittest.TestCase):
    def test_recorded_observation_preserves_acceptance_baseline_and_history(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "private.json"
            original = {"assigned": [{"slug": "example", "status": "in_progress"}, {"slug": "done", "status": "accepted"}],
                        "daily_baselines": {"date": {"docx_sha256": "immutable"}}, "checks": [{"result": "updated"}],
                        "profile": {"recent_accepted": [{"slug": "old"}]}}
            path.write_text(json.dumps(original))
            observation = {"available": True, "observed_at": "2026-10-08T05:00:00+08:00", "source": "synthetic public profile",
                           "solved_counts": [{"difficulty": "All", "count": 3}],
                           "recent_accepted": [{"slug": "example", "title": "Example", "statusDisplay": "Accepted"}]}
            self.assertTrue(workflow.record_profile(path, observation))
            workflow.record_profile(path, observation)
            updated = json.loads(path.read_text())
            self.assertEqual(updated["daily_baselines"], original["daily_baselines"])
            self.assertEqual(updated["checks"], original["checks"])
            self.assertEqual([a["status"] for a in updated["assigned"]], ["in_progress", "accepted"])
            self.assertEqual(len(updated["profile"]["observed_progress"]), 1)
            self.assertEqual({a["slug"] for a in updated["profile"]["recent_accepted"]}, {"old", "example"})
            before = path.read_bytes()
            self.assertFalse(workflow.record_profile(path, {"available": False}))
            self.assertEqual(path.read_bytes(), before)

    def test_utc_midnight_and_check(self):
        self.assertEqual(workflow.due_slot("2026-10-07T16:00:50Z")["date"], "2026-10-08")
        self.assertEqual(workflow.due_slot("2026-10-07T16:00:50Z")["phase"], "midnight")
        self.assertEqual(workflow.due_slot("2026-10-07T21:00:50Z")["phase"], "check")

    def test_early_late_and_explicit(self):
        self.assertEqual(workflow.due_slot("2026-10-07T15:56:17Z")["date"], "2026-10-08")
        self.assertEqual(workflow.due_slot("2026-10-07T18:00:00Z")["phase"], "midnight")
        self.assertEqual(workflow.due_slot("2026-10-08T02:28:09Z")["phase"], "check")
        self.assertEqual(workflow.due_slot("2026-10-08T02:28:09Z", "midnight", "2026-10-07")["date"], "2026-10-07")
        with self.assertRaises(ValueError):
            workflow.due_slot("2026-10-08T00:00:00")

    def test_all_history_is_excluded_not_just_assigned(self):
        ledger = {"assigned": [{"slug": "first", "status": "accepted"}], "accepted": ["second"],
                  "skipped": [{"slug": "third"}],
                  "profile": {"recent_accepted": [{"titleSlug": "fourth"}],
                              "observed_progress": [{"recent_accepted_in_screenshot": ["fifth"]}]}}
        self.assertEqual(workflow.used_slugs(ledger), ["fifth", "first", "fourth", "second", "third"])

    def test_selection_reuses_and_excludes_repeats(self):
        ledger = {"assigned": [{"date": "2026-10-08", "slug": "old"}]}
        candidates = [{"slug": "old", "difficulty": "Easy"}, {"slug": "new", "difficulty": "Medium"},
                      {"slug": "hard", "difficulty": "Hard"}]
        self.assertTrue(workflow.pick(ledger, candidates, "2026-10-08")["reused"])
        self.assertEqual(workflow.pick(ledger, candidates, "2026-10-09")["selection"]["slug"], "new")
        with self.assertRaises(ValueError):
            workflow.pick(ledger, candidates[:1], "2026-10-09")

    def test_extract_code_without_private_labeled_notes(self):
        lines = ["First Instinct | Why?", "```python", "class Solution:",
                 "    def solve(self):", "        return 1", "```", "Notes: private reflection", "Completion Check"]
        self.assertNotIn("private", sync.solution_code(lines))
        self.assertNotIn("```", sync.solution_code(lines))
        self.assertIn("return 1", sync.solution_code(lines))

    def test_multiple_versions_fail_closed(self):
        lines = ["First Instinct", "class Solution:", "    pass", "class Solution:", "    pass", "Completion Check"]
        with self.assertRaises(ValueError):
            sync.solution_code(lines)
        self.assertEqual(workflow.inspect_entry(lines)["code_outcome"], "invalid_or_ambiguous_python")

    def test_separate_fenced_versions_are_not_silently_selected(self):
        lines = ["First Instinct", "```python", "class Solution:", "    pass", "```",
                 "```python", "class Solution:", "    pass", "```", "Completion Check"]
        with self.assertRaises(ValueError):
            sync.solution_code(lines)

    def test_bad_python_never_silently_truncated(self):
        lines = ["First Instinct", "class Solution:", "    def solve(self):", "        return 1",
                 "        if", "Completion Check"]
        with self.assertRaises(SyntaxError):
            sync.solution_code(lines)

    def test_profile_failure_requires_browser(self):
        with patch.object(workflow, "urlopen", side_effect=OSError):
            self.assertTrue(workflow.public_profile("example")["browser_fallback_required"])

    def test_profile_does_not_confirm_learner_acceptance(self):
        payload = {"data": {"matchedUser": {"submitStatsGlobal": {"acSubmissionNum": [{"difficulty": "All", "count": 1}]}},
                            "recentAcSubmissionList": [{"title": "Example", "titleSlug": "example", "timestamp": "1791388800"}]}}
        response = MagicMock()
        response.geturl.return_value = "https://leetcode.com/graphql/"
        response.read.return_value = json.dumps(payload).encode()
        with patch.object(workflow, "urlopen") as open_mock:
            open_mock.return_value.__enter__.return_value = response
            result = workflow.public_profile("example")
        self.assertTrue(result["available"])
        self.assertFalse(result["learner_acceptance_confirmed"])
        self.assertFalse(result["complete_solved_history"])


if __name__ == "__main__":
    unittest.main()
