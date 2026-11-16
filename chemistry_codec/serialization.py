"""
Module for serialization and deserialization of chemistry data.

This module provides functions to serialize and deserialize reaction data,
including the chemical formula, reactants, products, and stoichiometry.
"""

import struct

def encode_version(version):
    """Encode version number as a 4-byte integer."""
    return struct.pack('>I', version)

def decode_version(data):
    """Decode version number from 4-byte integer."""
    return struct.unpack('>I', data)[0]

def encode_formula(formula):
    """
    Encode chemical formula as a string.

    The formula is encoded as a null-terminated string.
    """
    return (formula + '\x00').encode('utf-8')

def decode_formula(data):
    """Decode chemical formula from null-terminated string."""
    return data.decode('utf-8').rstrip('\x00')

def encode_reactants(reactants):
    """
    Encode reactant list as a list of strings.

    Each reactant is encoded as a null-terminated string.
    """
    return b''.join((r + '\x00').encode('utf-8') for r in reactants)

def decode_reactants(data):
    """Decode reactant list from null-terminated strings."""
    return [d.decode('utf-8').rstrip('\x00') for d in data.split(b'\x00')]

def encode_products(products):
    """
    Encode product list as a list of strings.

    Each product is encoded as a null-terminated string.
    """
    return b''.join((p + '\x00').encode('utf-8') for p in products)

def decode_products(data):
    """Decode product list from null-terminated strings."""
    return [d.decode('utf-8').rstrip('\x00') for d in data.split(b'\x00')]

def encode_stoichiometry(stoichiometry):
    """
    Encode stoichiometry as a dictionary of floats.

    Each value is encoded as a 4-byte float.
    """
    return b''.join(struct.pack('>f', v) for v in stoichiometry.values())

def decode_stoichiometry(data):
    """Decode stoichiometry from 4-byte floats."""
    return {i: struct.unpack('>f', data[i*4:i*4+4])[0] for i in range(len(data)//4)}
