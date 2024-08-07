#!/usr/bin/python3

"""A class that inherits from list"""


class MyList(list):
    """defining a method thats sorts a list"""
    def __init__(self):
        super().__init__

    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
