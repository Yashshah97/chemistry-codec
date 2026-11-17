"""Smoke tests for deserialization."""
import unittest

from chemistry_codec import deserialization


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(deserialization, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(deserialization) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
