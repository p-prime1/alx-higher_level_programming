#!/usr/bin/python3
"""Script takes in an argument form command line and 
    sends a post request with a letter with the argument as parameter"""


if __name__ == "__main__":
    import sys
    import requests

    data = {}
    try:
        data['q'] = sys.argv[1]
    except IndexError:
        data['q'] = ""

    r = requests.post("http://0.0.0.0:5000/search_user", data)
    try:
        resp = r.json()
        if resp == {}:
            print(f"No result")
        else:
            print(f"{[resp.get('id')]} {resp.get('name')}")
    except requests.exceptions.JSONDecodeError as e:
        print(f"Not a valid JSON")
