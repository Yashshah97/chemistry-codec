"""Demo for Chemistry Binary Codec."""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import chemistry_codec

print("Chemistry Binary Codec", "v" + chemistry_codec.__version__)
print("modules:", [m for m in dir(chemistry_codec) if not m.startswith('_')])
