#!/usr/bin/python3
"""
Module 5-save_to_json_file
Contains a function that writes an object to a text file using a JSON representation.
"""

import json

def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using JSON representation.

    Args:
        my_obj (object): Python object to serialize.
        filename (str): File path to write the JSON representation.

    Behavior:
        - Uses the 'with' statement to open the file.
        - Serializes the object using json.dump().
        - Overwrites the file if it already exists.
        - Does not handle exceptions if object is not serializable.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
