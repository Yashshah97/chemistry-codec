"""
Unit tests for the Chemistry Binary Codec implementation.

This module contains unit tests for the binary codec's serialization and deserialization functionality.
"""

import unittest
from dataclasses import FrozenInstanceError
from typing import Any

class TestCodec(unittest.TestCase):
    def test_versioning(self) -> None:
        """Test that versioning works correctly."""
        from chemistry_codec.codec import Codec, Version
        codec = Codec(Version(1))
        data = {"a": 1}
        serialized = codec.serialize(data)
        deserialized = codec.deserialize(serialized)
        self.assertEqual(deserialized, data)

    def test_frozen_instance_error(self) -> None:
        """Test that FrozenInstanceError is raised when trying to modify a frozen instance."""
        from chemistry_codec.codec import Codec
        codec = Codec(Version(1))
        data = {"a": 1}
        serialized = codec.serialize(data)
        with self.assertRaises(FrozenInstanceError):
            codec.deserialize(serialized).__dict__['a'] = 2

    def test_invalid_version(self) -> None:
        """Test that deserialization fails when version is invalid."""
        from chemistry_codec.codec import Codec, Version
        codec = Codec(Version(1))
        data = {"a": 1}
        serialized = codec.serialize(data)
        with self.assertRaises(ValueError):
            codec.deserialize(serialized, version=2)

    def test_invalid_data(self) -> None:
        """Test that deserialization fails when data is invalid."""
        from chemistry_codec.codec import Codec
        codec = Codec(Version(1))
        with self.assertRaises(TypeError):
            codec.deserialize(b'invalid')

if __name__ == '__main__':
    unittest.main()
