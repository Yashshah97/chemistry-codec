import unittest
from chemistry_codec import deserialization
import struct

class TestDeserialization(unittest.TestCase):

    def test_parse_int(self):
        buffer = b'\x00\x00\x00\x01'
        self.assertEqual(deserialization._parse_int(buffer), 1)

    def test_parse_float(self):
        buffer = b'\x3f\x80\x00\x00'
        self.assertAlmostEqual(deserialization._parse_float(buffer), 1.0)

    def test_deserialize(self):
        buffer = b'\x12\x34\x56\x78\x01\x00\x00\x00\x01\x00\x00\x00\x02\x08\x3f\x80\x00\x00'
        data = deserialization.deserialize(buffer, 1)
        self.assertEqual(data['reaction_id'], 1)
        self.assertEqual(data['coefficients'], [1.0])

    def test_deserialize_invalid_magic(self):
        buffer = b'\x12\x34\x56\x79\x01\x00\x00\x00'
        with self.assertRaises(ValueError):
            deserialization.deserialize(buffer, 1)

if __name__ == '__main__':
    unittest.main()
