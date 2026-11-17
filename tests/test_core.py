import unittest
from chemistry_codec import core

class TestCore(unittest.TestCase):
    def test_encode_decode(self):
        reaction = {'H2': 1.0, 'O2': 1.0}
        encoded_data = core.encode_reaction(reaction)
        decoded_reaction = core.decode_reaction(encoded_data)
        self.assertEqual(reaction, decoded_reaction)

    def test_decode_invalid_version(self):
        encoded_data = b'\x00\x00\x00\x02' + b'\x01'
        with self.assertRaises(ValueError):
            core.decode_reaction(encoded_data)

if __name__ == '__main__':
    unittest.main()
