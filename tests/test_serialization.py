import unittest
from chemistry_codec import serialization

class TestSerialization(unittest.TestCase):
    def test_encode_version(self):
        self.assertEqual(serialization.encode_version(1), b'\x00\x00\x00\x01')

    def test_decode_version(self):
        self.assertEqual(serialization.decode_version(b'\x00\x00\x00\x01'), 1)

    def test_encode_formula(self):
        self.assertEqual(serialization.encode_formula('H2O'), b'H2O\x00')

    def test_decode_formula(self):
        self.assertEqual(serialization.decode_formula(b'H2O\x00'), 'H2O')

    def test_encode_reactants(self):
        self.assertEqual(serialization.encode_reactants(['H2', 'O2']), b'H2\x00O2\x00')

    def test_decode_reactants(self):
        self.assertEqual(serialization.decode_reactants(b'H2\x00O2\x00'), ['H2', 'O2'])

    def test_encode_products(self):
        self.assertEqual(serialization.encode_products(['CO2', 'H2O']), b'CO2\x00H2O\x00')

    def test_decode_products(self):
        self.assertEqual(serialization.decode_products(b'CO2\x00H2O\x00'), ['CO2', 'H2O'])

    def test_encode_stoichiometry(self):
        stoich = {'A': 1.0, 'B': 2.0}
        expected = b'\x3f\x99\x99\x99\xbf\xbf\xbf\xbf'
        self.assertEqual(serialization.encode_stoichiometry(stoich), expected)

    def test_decode_stoichiometry(self):
        data = b'\x3f\x99\x99\x99\xbf\xbf\xbf\xbf'
        self.assertEqual(serialization.decode_stoichiometry(data), {'A': 1.0, 'B': 2.0})

if __name__ == '__main__':
    unittest.main()
