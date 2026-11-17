from typing import Dict, List, Tuple

def encode_reaction(reaction: Dict[str, float]) -> bytes:
    """
    Encode a reaction into a compact binary format.

    :param reaction: A dictionary of reactants and products with stoichiometry.
    :return: The encoded reaction as bytes.
    """
    # Convert the reaction to a tuple of (formula, amount) pairs
    items = [(k, v) for k, v in reaction.items()]
    
    # Sort the items by formula length to ensure reproducibility
    items.sort(key=lambda x: len(x[0]))
    
    # Encode each item as a 4-byte formula and 8-byte float
    encoded_items = []
    for formula, amount in items:
        encoded_formula = formula.encode('utf-8')
        encoded_amount = amount.to_bytes(8, 'big', signed=True)
        encoded_items.append((len(encoded_formula), encoded_formula) + (encoded_amount,))
    
    # Write the version and number of items as 4-byte integers
    encoded_version = 1
    encoded_num_items = len(encoded_items)
    
    # Encode the data into a single byte string
    encoded_data = (
        encoded_version.to_bytes(4, 'big', signed=True) +
        encoded_num_items.to_bytes(4, 'big', signed=True) +
        b''.join(
            (len(item[1]).to_bytes(4, 'big', signed=True), item[1]) + item[2:]
            for item in encoded_items
        )
    )
    
    return encoded_data

def decode_reaction(encoded_data: bytes) -> Dict[str, float]:
    """
    Decode a reaction from a compact binary format.

    :param encoded_data: The encoded reaction as bytes.
    :return: A dictionary of reactants and products with stoichiometry.
    """
    # Unpack the version and number of items
    encoded_version = int.from_bytes(encoded_data[:4], 'big', signed=True)
    encoded_num_items = int.from_bytes(encoded_data[4:8], 'big', signed=True)
    
    if encoded_version != 1:
        raise ValueError("Unsupported version")
    
    # Unpack the data into a list of (formula, amount) pairs
    offset = 8
    items = []
    for _ in range(encoded_num_items):
        formula_length = int.from_bytes(encoded_data[offset:offset+4], 'big', signed=True)
        encoded_formula = encoded_data[offset+4:offset+4+formula_length]
        encoded_amount = int.from_bytes(encoded_data[offset+4+formula_length:], 8, 'big', signed=True)
        items.append((encoded_formula.decode('utf-8'), encoded_amount))
        offset += formula_length + 8
    
    # Convert the list of (formula, amount) pairs to a dictionary
    reaction: Dict[str, float] = dict(items)
    
    return reaction

def test_encode_decode() -> None:
    """
    Test the encode and decode functions.

    :return: None
    """
    reaction = {'H2': 1.0, 'O2': 1.0}
    encoded_data = encode_reaction(reaction)
    decoded_reaction = decode_reaction(encoded_data)
    
    assert reaction == decoded_reaction

if __name__ == '__main__':
    test_encode_decode()
