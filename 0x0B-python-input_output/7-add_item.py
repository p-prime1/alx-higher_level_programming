#!/usr/bin/python3

"""This module adds argument to a Python list and saves them to a
JSON file"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def save_to_file():
    """The function accepts command line arguments and saves them
    to a JSON file"""

    filename = 'add_item.json'
    try:
        item = load_from_json_file(filename)
    except (FileNotFoundError, json.JSONDecodeError):
        item = []
    item.extend(sys.argv[1:])
    save_to_json_file(item, filename)


if __name__ == '__main__':
    save_to_file()
