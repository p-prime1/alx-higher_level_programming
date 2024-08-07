#!/usr/bin/python3
"""Checks if an object is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """Returns true if its an instance and false if its not
        obj (object): Object to be checked
        a_class (Class): The class to be compared
        """
    if type(obj) is a_class or isinstance(obj, a_class):
        return (True)
    return (False)
