#!/usr/bin/python3
"""
Module 2-append_write
Contains a function that appends a UTF-8 text string to a file
and returns the number of characters added.
"""

def append_write(filename="", text=""):
    """
    Appends a string to a text file (UTF-8) and returns the number of characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text content to append to the file.

    Returns:
        int: Number of characters added to the file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
