#!/usr/bin/python3
"""Modules sends request to a url and displays the value of a header
variable"""


if __name__ == "__main__":
    import requests
    import sys

    resp = requests.get(sys.argv[1])
    print(resp.headers['X-Request-Id'])
