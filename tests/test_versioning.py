"""Smoke tests for versioning."""
import unittest

from chemistry_codec import versioning


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(versioning, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(versioning) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
