import subprocess
import sys
import unittest


def run(text):
    return subprocess.run(
        [sys.executable, "time.py"], input=text, capture_output=True, text=True
    )


class HomeworkTests(unittest.TestCase):
    def test_total(self):
        out = run("math\nenglish\ndone\n10\n20\n")
        self.assertEqual(out.returncode, 0)
        self.assertIn("It will take you 30 minutes", out.stdout)

    def test_done_is_case_insensitive_and_nan_is_rejected_then_retried(self):
        out = run("math\nDone\nnan\n15\n")
        self.assertEqual(out.returncode, 0)
        self.assertIn("finite", out.stdout)
        self.assertIn("It will take you 15 minutes", out.stdout)

    def test_negative_is_rejected_then_retried(self):
        out = run("math\ndone\n-5\n5\n")
        self.assertEqual(out.returncode, 0)
        self.assertIn("zero or more", out.stdout)
        self.assertIn("It will take you 5 minutes", out.stdout)

    def test_eof_during_times_exits_1_without_partial_total(self):
        out = run("math\nenglish\ndone\n10\n")
        self.assertEqual(out.returncode, 1)
        self.assertIn("Input ended before all times were entered.", out.stdout)
        self.assertNotIn("It will take you", out.stdout)

    def test_empty_list_totals_zero(self):
        out = run("done\n")
        self.assertEqual(out.returncode, 0)
        self.assertIn("It will take you 0 minutes", out.stdout)


if __name__ == "__main__":
    unittest.main()
