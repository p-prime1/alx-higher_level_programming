#!/usr/bin/python3

"""Checks if an object is an instance of a class or a subclass"""


def inherits_from(obj, a_class):
    """Functions accepts two arguments:
        obj (object): An object to be checked
        a_class (Class): A class to check if obj is an instance or subclass
    """
    if isinstance(obj, a_class):
        return (True)
    return (False)
