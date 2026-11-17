import tempfile
import unittest
from pathlib import Path
from yaml_sentry.loader import inspect_yaml

class LoaderTests(unittest.TestCase):
    def test_duplicate_key_reports_second_line(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "sample.yaml"
            path.write_text("app:\n  port: 80\n  port: 81\n", encoding="utf-8")
            issues = inspect_yaml(path)
            self.assertEqual(len(issues), 1)
            self.assertEqual(issues[0]["line"], 3)
            self.assertIn("duplicate key", issues[0]["message"])

    def test_valid_yaml_has_no_issues(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "valid.yaml"
            path.write_text("app:\n  port: 80\n", encoding="utf-8")
            self.assertEqual(inspect_yaml(path), [])

if __name__ == "__main__":
    unittest.main()
