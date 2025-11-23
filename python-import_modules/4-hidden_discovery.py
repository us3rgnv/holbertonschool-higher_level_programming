#!/usr/bin/python3
# This script prints all names in hidden_4.pyc that do not start with __

import dis
import marshal

with open("/tmp/hidden_4.pyc", "rb") as f:
    f.read(16)  # skip header
    code = marshal.load(f)

names = [name for name in code.co_names if not name.startswith("__")]

for name in sorted(names):
    print(name)
