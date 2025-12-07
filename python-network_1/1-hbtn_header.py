#!/usr/bin/python3
"""Fetch a URL and print the value of the X-Request-Id header."""
from urllib import request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with request.urlopen(url) as response:
        # getheader returns None if header is not present
        x_request_id = response.getheader("X-Request-Id")
    if x_request_id is not None:
        print(x_request_id)
