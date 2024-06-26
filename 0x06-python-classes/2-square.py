#!/usr/bin/python3

"""Defines a square"""


class Square:
    """Represents a aquare"""

    def __init__(self, size=0):
        """Initializes a square.
            Args:
                size (int): The size of the new square.
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
