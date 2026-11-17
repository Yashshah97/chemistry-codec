"""
Module handling versioning of the codec.

This module is responsible for serializing and deserializing versions of the codec.
"""

class Version:
    """
    A single version of the codec.

    Attributes:
        major (int): The major version number.
        minor (int): The minor version number.
        patch (int): The patch version number.
    """

    def __init__(self, major, minor, patch):
        self.major = major
        self.minor = minor
        self.patch = patch

    @classmethod
    def from_bytes(cls, data):
        """
        Deserialize a version from bytes.

        Args:
            data (bytes): The serialized version data.

        Returns:
            Version: The deserialized version.
        """
        major, minor, patch = struct.unpack('>3i', data)
        return cls(major, minor, patch)

    def to_bytes(self):
        """
        Serialize the version as bytes.

        Returns:
            bytes: The serialized version data.
        """
        return struct.pack('>3i', self.major, self.minor, self.patch)


def serialize_version(version):
    """
    Serialize a version as bytes.

    Args:
        version (Version): The version to serialize.

    Returns:
        bytes: The serialized version data.
    """
    return version.to_bytes()


def deserialize_version(data):
    """
    Deserialize a version from bytes.

    Args:
        data (bytes): The serialized version data.

    Returns:
        Version: The deserialized version.
    """
    return Version.from_bytes(data)


import struct
