#!/usr/bin/python3
"""
Module 0-read_file
Contains a function that reads a UTF-8 text file and prints it to stdout.
"""

def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints it to stdout.

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
