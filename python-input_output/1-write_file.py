#!/usr/bin/python3
"""
Module 1-write_file
Contains a function that writes a UTF-8 text string to a file
and returns the number of characters written.
"""

def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8) and returns the number of characters written.

    Args:
        filename (str): The name of the file to write.
        text (str): The text content to write to the file.

    Returns:
        int: Number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
