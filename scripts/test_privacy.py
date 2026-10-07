"""Exercise publishing privacy guards using synthetic values only."""

from pathlib import Path
import tempfile
import unittest

from privacy import scan_public_tree, scan_text


class PrivacyTests(unittest.TestCase):
    def test_credentials_are_blocked(self):
        values = ["ghp_" + "a" * 36, "sk-proj-" + "b" * 40, "AKIA" + "C" * 16,
                  "https://example:" + "credential" + "@" + "example.com", "/Users/" + "example/private/",
                  "example" + "@private.example", "password = " + repr("synthetic-value")]
        for value in values:
            self.assertTrue(scan_text(value))

    def test_private_file_is_blocked(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "data").mkdir()
            (root / "data/journal.docx").write_bytes(b"synthetic")
            with self.assertRaises(ValueError):
                scan_public_tree(root)

    def test_public_code_passes(self):
        self.assertFalse(scan_text("class Solution:\n    def solve(self, nums):\n        return len(nums)\n"))

    def test_workflow_is_scanned_and_symlink_parents_blocked(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            workflow = root / ".github/workflows/validate.yml"
            workflow.parent.mkdir(parents=True)
            workflow.write_text("token: " + "ghp_" + "a" * 36)
            with self.assertRaises(ValueError):
                scan_public_tree(root)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / ".github").symlink_to(root / "other", target_is_directory=True)
            with self.assertRaises(ValueError):
                scan_public_tree(root)


if __name__ == "__main__":
    unittest.main()
