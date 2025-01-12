#!/usr/bin/python3
"""Script fetches a url and returns info of the page"""


if __name__ == "__main__":
    import urllib.request

    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        resp = response.read()
        print(f"""Body response:
            - type: {type(resp)}
            - content: {resp}
            - utf8 content: {resp.decode('utf-8')}""")
