#!/usr/bin/python3

"""This module writes an object to a file using JSON representation"""


import json


def save_to_json_file(my_obj=None, filename=None):
    """Converts a Python object to a JSON string and writes it to a file
    using the mode.

    The function Creates the file if it doesnt exit and overwrites it if
    it does.

    Args:
        my_obj (object): Object to be conerted to JSON
        filename (str): Name of file
    """
    text = json.dumps(my_obj)
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(text)
