# arg_parser.py

import sys
import hashlib

if len(sys.argv) > 1:
    print(f"Argument: {sys.argv[1]}")
    hash_obj = hashlib.sha256(sys.argv[1].encode())
    print(f"SHA256: {hash_obj.hexdigest()}")
else:
    print("Usage: python arg_parser.py <string>")
