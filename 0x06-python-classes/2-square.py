#!/usr/bin/python3

"""Defines a square"""


class Square:
    """Represents a aquare"""

    def __init__(self, size=0):
        """Initializes a square.
            Args:
                size (int): The size of the new square.
        """
        self.__size = size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size <= 0:
            raise ValueError("size must be >= 0")
