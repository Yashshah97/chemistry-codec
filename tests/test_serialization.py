"""Smoke tests for serialization."""
import unittest

from chemistry_codec import serialization


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(serialization, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(serialization) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
