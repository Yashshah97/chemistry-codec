import unittest
from chemistry_codec import versioning

class TestVersioning(unittest.TestCase):
    def test_version_init(self):
        v = versioning.Version(1, 2, 3)
        self.assertEqual(v.major, 1)
        self.assertEqual(v.minor, 2)
        self.assertEqual(v.patch, 3)

    def test_version_from_bytes(self):
        data = b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00'
        v = versioning.Version.from_bytes(data)
        self.assertEqual(v.major, 1)
        self.assertEqual(v.minor, 2)
        self.assertEqual(v.patch, 3)

    def test_version_to_bytes(self):
        v = versioning.Version(1, 2, 3)
        data = v.to_bytes()
        self.assertEqual(data, b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00')

    def test_serialize_version(self):
        v = versioning.Version(1, 2, 3)
        data = versioning.serialize_version(v)
        self.assertEqual(data, b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00')

    def test_deserialize_version(self):
        data = b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00'
        v = versioning.deserialize_version(data)
        self.assertEqual(v.major, 1)
        self.assertEqual(v.minor, 2)
        self.assertEqual(v.patch, 3)

if __name__ == '__main__':
    unittest.main()
