#!/usr/bin/python3
"""
Script that takes your GitHub credentials and displays your id
using the GitHub API
"""

import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"

    try:
        response = requests.get(url, auth=(username, token))
        if response.status_code == 200:
            data = response.json()
            print(data.get('id'))
        else:
            print(None)
    except requests.exceptions.RequestException:
        print(None)
