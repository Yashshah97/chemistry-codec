# Architecture Plan

- `chemistry_codec/chemistry_binary_codec.py` — Main entry point and top-level module for the Chemistry Binary Codec
- `chemistry_codec/serialization.py` — Module responsible for serializing and deserializing data to/from binary format
- `chemistry_codec/deserialization.py` — Module responsible for parsing serialized data from binary format
- `chemistry_codec/versioning.py` — Module handling versioning of the codec, including serialization and deserialization of versions
- `chemistry_codec/tests_test_codec.py` — Unit tests for the Chemistry Binary Codec implementation
- `chemistry_codec/core.py` — main domain logic and public entry points
