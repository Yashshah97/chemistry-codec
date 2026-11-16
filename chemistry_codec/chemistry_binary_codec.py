"""
Chemistry Binary Codec — A binary codec for reaction balancing and stoichiometry.

A compact binary serialization format with versioning.

This is the main entry point and top-level module for the Chemistry Binary Codec.
"""

from typing import Any, Dict, List, Tuple

def encode_version(version: int) -> bytes:
    """Encode a version number as a 4-byte integer."""
    return version.to_bytes(4, 'big')

def decode_version(data: bytes) -> int:
    """Decode a version number from 4 bytes."""
    return int.from_bytes(data, 'big')

def encode_struct(struct: Dict[str, Any]) -> bytes:
    """Encode a struct as a series of key-value pairs."""
    data = b''
    for key, value in struct.items():
        data += key.encode('utf-8') + b'\x00'
        if isinstance(value, int):
            data += encode_version(value)
        elif isinstance(value, float):
            data += value.to_bytes(8, 'big')
        else:
            raise ValueError("Unsupported type")
    return data

def decode_struct(data: bytes) -> Dict[str, Any]:
    """Decode a struct from a series of key-value pairs."""
    struct = {}
    i = 0
    while i < len(data):
        key_len = data.find(b'\x00', i)
        if key_len == -1:
            raise ValueError("Invalid data")
        key = data[i:key_len].decode('utf-8')
        value_type = data[key_len+1]
        if value_type == 0: # int
            struct[key] = decode_version(data[key_len+2:key_len+6])
        elif value_type == 1: # float
            struct[key] = int.from_bytes(data[key_len+2:key_len+10], 'big')
        i = key_len + 1
    return struct

def encode_reaction(reaction: Dict[str, List[Tuple[int, str]]]) -> bytes:
    """Encode a reaction as a series of reactant-product pairs."""
    data = b''
    for reactants, products in reaction.items():
        data += encode_struct({'reactants': reactants, 'products': products})
    return data

def decode_reaction(data: bytes) -> Dict[str, List[Tuple[int, str]]]:
    """Decode a reaction from a series of reactant-product pairs."""
    reactions = {}
    i = 0
    while i < len(data):
        struct = decode_struct(data[i:])
        reactions[struct['reactants']] = struct['products']
        i += encode_version(len(struct)).length + 1
    return reactions

# Example usage:
if __name__ == '__main__':
    reaction = {
        'H2O': [(2, 'H'), (1, 'O')],
        'CO2': [(1, 'C'), (2, 'O')]
    }
    encoded_reaction = encode_reaction(reaction)
    print(encode_version(1))  # version number
    print(encoded_reaction)  # encoded reaction data
