#!/usr/bin/python3
"""
Function that returns the dictionary description
with simple data structures for JSON serialization of an object.
"""

def class_to_json(obj):
    """
    Returns the dictionary representation of an object
    with attributes that are serializable (list, dict, str, int, bool).

    Args:
        obj: instance of a class

    Returns:
        dict: dictionary of serializable attributes of obj
    """
    return obj.__dict__.copy()
