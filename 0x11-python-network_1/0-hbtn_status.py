#!/usr/bin/python3
"""Script fetches a url and returns info of the page"""


if __name__ == "__main__":
    import urllib.request

    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        resp = response.read()
        print(f"Body response:")
        print(f"\t- type: {type(resp)}")
        print(f"\t- content: {resp}")
        print(f"\t- utf8 content: {resp.decode('utf-8')}")
