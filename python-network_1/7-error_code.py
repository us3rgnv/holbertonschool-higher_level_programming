#!/usr/bin/python3
"""Sends a request to a URL and displays the body or error code"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        response = requests.get(url)
        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")
        else:
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
