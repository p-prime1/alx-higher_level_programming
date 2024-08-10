#!/usr/bin/python3


"""This module converts a JSON string into a Python object"""


import json


def from_json_string(my_str):
    """Converts a JSON string to a Python object
    Args:
        my_str (str): String to be converted

    Returns (object):
        Returns an object derived form the JSON string
    """
    return (json.loads(my_str))
