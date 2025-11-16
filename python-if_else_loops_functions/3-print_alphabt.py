#!/usr/bin/python3
# This script prints the ASCII alphabet in lowercase except q and e

for c in range(97, 123):
    if c != 101 and c != 113:
        print("{}".format(chr(c)), end="")
