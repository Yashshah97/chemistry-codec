import unittest
from chemistry_codec import tests_test_codec

class TestTestsTestCodec(unittest.TestCase):
    def test_module_exists(self) -> None:
        """Test that the module exists."""
        self.assertTrue(hasattr(tests_test_codec, '__name__'))

    def test_module_is_package(self) -> None:
        """Test that the module is a package."""
        self.assertTrue(hasattr(tests_test_codec, '__package__'))

if __name__ == '__main__':
    unittest.main()
