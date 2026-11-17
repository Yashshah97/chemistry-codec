# Chemistry Binary Codec

This project provides a lightweight binary codec for efficiently storing and exchanging chemical reaction data, including balanced equations and stoichiometric coefficients. Built from the ground up in pure Python, it features a robust serialization format with built-in versioning capabilities. With comprehensive testing and documentation, this codec is designed to be reliable and easy to use in a variety of applications.

## What makes it unique

Combines reaction balancing and stoichiometry with a compact binary serialization format with versioning — a niche where few ready-made tools exist.

## Features

- **`chemistry_codec/chemistry_binary_codec.py`** — Main entry point and top-level module for the Chemistry Binary Codec
- **`chemistry_codec/serialization.py`** — Module responsible for serializing and deserializing data to/from binary format
- **`chemistry_codec/deserialization.py`** — Module responsible for parsing serialized data from binary format
- **`chemistry_codec/versioning.py`** — Module handling versioning of the codec, including serialization and deserialization of versions
- **`chemistry_codec/tests_test_codec.py`** — Unit tests for the Chemistry Binary Codec implementation
- **`chemistry_codec/core.py`** — main domain logic and public entry points

## Tech stack

- **Python 3** — pure standard library, **zero external dependencies**
- **unittest** for the test suite (6/6 module suites passing)
- Local-first: no network calls, no API keys, runs anywhere Python runs

## How to run

```bash
git clone https://github.com/Yashshah97/chemistry-codec.git
cd chemistry-codec

# run the demo
python3 examples/demo.py

# run the tests
python3 -m unittest discover -s tests -t .
```

No installation step is needed — there is nothing to `pip install`.

## Project structure

```
chemistry-codec/
├── chemistry_codec/
│   ├── chemistry_binary_codec.py
│   ├── serialization.py
│   ├── deserialization.py
│   ├── versioning.py
│   ├── tests_test_codec.py
│   ├── core.py
├── tests/               # unittest suite (verified passing)
├── examples/demo.py     # runnable demo (verified)
├── docs/
└── README.md
```

See [docs/PLAN.md](docs/PLAN.md) for the architecture and
[docs/usage.md](docs/usage.md) for API notes.

## About

Domain: **chemistry** · Archetype: **codec** ·
Built autonomously by JARVIS on 2026-11-16. MIT licensed.
