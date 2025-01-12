#!/usr/bin/python3
"""Scripts sends a url and displays the body, handles http errors also"""


if __name__ == "__main__":
    import requests
    import sys

    resp = requests.get(sys.argv[1])
    if resp.status_code >= 400:
        print(f"Error code: {resp.status_code}")
    else:
        print(resp.text)
