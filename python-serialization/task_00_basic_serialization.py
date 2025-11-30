#!/usr/bin/python3
""" Basic serialization module
"""

import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it to a JSON file.
    
    Args:
        data (dict): Python dictionary to serialize.
        filename (str): Name of the output JSON file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load and deserialize a JSON file to a Python dictionary.
    
    Args:
        filename (str): Name of the input JSON file.
    
    Returns:
        dict: Python dictionary with deserialized data.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
