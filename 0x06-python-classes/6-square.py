#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Rep Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the class with size and the postion tuple"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Returns the size variable"""
        size = self.__size
        return (size)

    @size.setter
    def size(self, value):
        """Sets the Size Variable"""
        if value is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Returns the position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Sets the value for the positions"""
        for i in value:
            if i < 0:
                raise TypeError("position must be a tuple of 2 positive integers""")
        self.__position = value

    def area(self):
        """Returns the Square Area"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square to thre STDOUT"""
        size = self.__size
        position = self.__position
        if size <= 0:
            print("")
        i = 0
        while i < size:
            print(" " * position[1], end="")
            print("#" * size, end="")
            i+=1

