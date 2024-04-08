#!/usr/bin/python3

"""Defines a class Square"""


class Square:
    """Rep an Area"""
    def __init__(self, size=0):
        """Initializes variables
        Args:
            size (int): Size of square
            """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area"""
        value = self.__size
        return value ** 2
