#!/usr/bin/python3
"""Send a POST request to a URL with an email parameter and display the response."""
from urllib import request, parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email data
    data = parse.urlencode({'email': email}).encode('utf-8')

    # Create a POST request
    req = request.Request(url, data=data)

    # Send the request and read the response
    with request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
