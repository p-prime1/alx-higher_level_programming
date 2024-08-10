#!/usr/bin/python3

"""This module creates a Python object from a JSON  file"""


import json


def load_from_json_file(filename):
    """The function reads from a file and converts the data
    into a Python Object

    Args:
        filename (str): Name of file

    Returns:
        obj: Returns an object
    """

    with open(filename, encoding='utf-8') as file:
        data = file.read()

    return (json.loads(data))
