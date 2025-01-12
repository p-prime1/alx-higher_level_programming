#!/usr/bin/python3
"""Script send request to a url using request"""


if __name__ == "__main__":
    import requests

    r = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print(f"\t - type: {type(r.text)}")
    print(f"\t - content: {r.text}")
