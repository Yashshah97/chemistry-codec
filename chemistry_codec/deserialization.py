"""
Module responsible for parsing serialized data from binary format.

This module contains functions to deserialize reaction balancing and stoichiometry data
from the binary format defined by the Chemistry Binary Codec.
"""

import struct

def _parse_int(buffer):
    """
    Parse an integer value from a buffer.

    :param buffer: bytes buffer containing the integer value
    :return: parsed integer value
    """
    return struct.unpack('>i', buffer[:4])[0]

def _parse_float(buffer):
    """
    Parse a float value from a buffer.

    :param buffer: bytes buffer containing the float value
    :return: parsed float value
    """
    return struct.unpack('>f', buffer[:4])[0]

def deserialize(buffer, version):
    """
    Deserialize reaction balancing and stoichiometry data from binary format.

    :param buffer: bytes buffer containing serialized data
    :param version: serialization format version
    :return: deserialized data (dict)
    """
    if len(buffer) < 8:
        raise ValueError("Invalid buffer length")

    magic, version_in_buffer = struct.unpack('>ii', buffer[:8])
    if magic != 0x12345678 or version_in_buffer != version:
        raise ValueError("Invalid serialization format")

    data = {}
    offset = 8
    while offset < len(buffer):
        tag = _parse_int(buffer[offset:offset+4])
        value_size = _parse_int(buffer[offset+4:offset+8])
        if tag == 1:  # reaction_id
            data['reaction_id'] = _parse_int(buffer[offset+8:offset+12])
        elif tag == 2:  # coefficients
            data['coefficients'] = [_parse_float(buffer[offset+12+i*4:offset+16+i*4]) for i in range(value_size)]
        offset += value_size * 4 + 12

    return data
