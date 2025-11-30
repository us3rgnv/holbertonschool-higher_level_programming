#!/usr/bin/python3
"""
Module 3-to_json_string
Contains a function that returns the JSON representation of an object as a string.
"""

import json

def to_json_string(my_obj):
    """
    Returns the JSON representation of a Python object (string).

    Args:
        my_obj (any): The object to convert to JSON string.

    Returns:
        str: JSON representation of the object.
    """
    return json.dumps(my_obj)
