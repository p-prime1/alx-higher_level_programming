#!/usr/bin/python3

"""Defines a new func that checks if an object is exactly an instance"""


def is_same_class(obj, a_class):
    """Function accepts two argument:
        obj (Object): An object to be checked
        a_class (Class): A class to check if its an instance"""

    if type(obj) is a_class:
        return (True)
    return (False)
