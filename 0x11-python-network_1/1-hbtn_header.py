#!/usr/bin/python3
"""Module takes in an argument and displays a header value from the response"""


if __name__ == "__main__":
    import urllib.request
    import sys

    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        header = response.headers
        print(header.get('X-Request-Id'))
