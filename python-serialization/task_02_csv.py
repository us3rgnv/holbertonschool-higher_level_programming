#!/usr/bin/python3
"""
Module to convert a CSV file into JSON format using serialization.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert the CSV file into a JSON file named data.json.
    
    Args:
        csv_filename (str): The name of the CSV file to convert.
    
    Returns:
        bool: True if conversion was successful, False otherwise.
    """
    try:
        with open(csv_filename, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            data = [row for row in reader]

        with open('data.json', 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4)

        return True
    except Exception:
        return False
