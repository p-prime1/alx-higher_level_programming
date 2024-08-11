#!/usr/bin/python3

"""Module returns a dictonary description of a class"""


def class_to_json(obj):
    """Returns the dictionary representation of a class.

    Args:
        obj (obj): Instance of a class

    Returns:
        Returns the dict rep of the instance of the class
    """
    return (obj.__dict__)
