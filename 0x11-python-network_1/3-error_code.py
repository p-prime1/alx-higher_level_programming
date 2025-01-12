#!/usr/bin/python3
"""Module send request and handles errors"""


if __name__ == "__main__":
    import urllib.error
    import urllib.request
    import sys

    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
            print(f"Error code: {e.code}")
