#!/usr/bin/python3
"""Module send a post Request using urllib"""


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    email = sys.argv[2]
    url = sys.argv[1]
    values = {'email': email}
    data = urllib.parse.urlencode(values).encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
