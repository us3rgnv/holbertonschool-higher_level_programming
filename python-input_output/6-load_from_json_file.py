#!/usr/bin/python3
"""
Module 6-load_from_json_file
Contains a function that creates a Python object from a JSON file.
"""

import json

def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file.

    Args:
        filename (str): Path to the JSON file.

    Returns:
        object: Python object represented by the JSON content.

    Behavior:
        - Uses the 'with' statement to open the file.
        - Reads the content and converts it from JSON to a Python object.
        - Does not handle exceptions for invalid JSON or missing file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
