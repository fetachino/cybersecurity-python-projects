import importlib.util
from pathlib import Path
import unittest


MODULE_PATH = Path(__file__).parents[1] / "substitution-cipher" / "substitution_cipher.py"
SPEC = importlib.util.spec_from_file_location("substitution_cipher", MODULE_PATH)
cipher = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(cipher)


class SubstitutionCipherTests(unittest.TestCase):
    def test_round_trip_preserves_text(self):
        message = "Meet me at 8:30 PM!"
        self.assertEqual(cipher.decode(cipher.encode(message)), message)

    def test_known_encoding(self):
        self.assertEqual(cipher.encode("ABC xyz"), "XPM iqv")

    def test_rejects_invalid_key(self):
        with self.assertRaises(ValueError):
            cipher.encode("message", "A" * 26)


if __name__ == "__main__":
    unittest.main()
