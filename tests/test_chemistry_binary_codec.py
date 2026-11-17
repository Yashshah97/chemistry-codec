"""Smoke tests for chemistry_binary_codec."""
import unittest

from chemistry_codec import chemistry_binary_codec


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(chemistry_binary_codec, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(chemistry_binary_codec) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
