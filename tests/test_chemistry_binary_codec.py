import unittest
from chemistry_codec import chemistry_binary_codec

class TestChemistryBinaryCodec(unittest.TestCase):
    def test_encode_version(self):
        self.assertEqual(chemistry_binary_codec.encode_version(1), b'\x00\x00\x00\x01')
        self.assertEqual(chemistry_binary_codec.encode_version(0), b'\x00\x00\x00\x00')

    def test_decode_version(self):
        self.assertEqual(chemistry_binary_codec.decode_version(b'\x00\x00\x00\x01'), 1)
        self.assertEqual(chemistry_binary_codec.decode_version(b'\x00\x00\x00\x00'), 0)

    def test_encode_struct(self):
        struct = {'a': 1, 'b': 2.5}
        expected_data = b'a\x00\x00\x00\x01b\x00\x00\x00\x00\x00\x00\x00\x00\x05'
        self.assertEqual(chemistry_binary_codec.encode_struct(struct), expected_data)

    def test_decode_struct(self):
        data = b'a\x00\x00\x00\x01b\x00\x00\x00\x00\x00\x00\x00\x00\x05'
        struct = chemistry_binary_codec.decode_struct(data)
        self.assertEqual(struct, {'a': 1, 'b': 2.5})

    def test_encode_reaction(self):
        reaction = {'H2O': [(2, 'H'), (1, 'O')], 'CO2': [(1, 'C'), (2, 'O')]}
        expected_data = b'\x00\x01' + chemistry_binary_codec.encode_struct({'reactants': ['H2O', 'CO2'], 'products': [[2, 'H'], [1, 'O']]}).decode('utf-8')
        self.assertEqual(chemistry_binary_codec.encode_reaction(reaction), expected_data)

if __name__ == '__main__':
    unittest.main()
