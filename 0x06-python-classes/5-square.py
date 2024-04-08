#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Rep Square"""

    def __init__(self, size=0):
        """Initializes the fields
        Args:
            size (int): Size of square
            """
        self.__size = size

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of size
        Args:
            value (int): Value to be assigned to size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square"""
        value = self.area()
        size = self.__size
        if size == 0:
            print("")
        else:
            for i in range(size):
                print("#" * size)
