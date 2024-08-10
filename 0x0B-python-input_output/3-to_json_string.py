#!/usr/bin/python3

"""This module provides a funtion that returns a json
representation of an object"""


import json


def to_json_string(my_obj):
    """Converts a Python object to a JSON string.
    Args:
        my_obj (object): Object to be converted

    Returns:
        str: Returns the JSON representation of the object.
    """
    return (json.dumps(my_obj))
