#!/usr/bin/python3
"""Module send a post request with a parameter"""


if __name__ == "__main__":
    import requests
    import sys

    data = {"email": sys.argv[2]}
    resp = requests.post(sys.argv[1], data)
    print(resp.text)
