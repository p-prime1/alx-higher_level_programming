#!/usr/bin/python3

"""Defines a geometry class"""


class BaseGeometry:
    """An area method"""
    def area(self):
        """Raises an error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value if its an integer
        Arguments:
            name (String): Name
            value (int): Integer to be validated
            """
        if value is not int:
            raise TypeError("<name> must be an integer")
        elif value <= 0:
            raise ValueError("<name> must be greater than 0")


"""A rectangle a class that inherits form BaseGeometry"""


class Rectangle(BaseGeometry):
    """Intializes the class"""
    def __init__(self, width, height):
        """Initializes the parent class and validates for int using the integer
        using the integer_validator func from parent class
        Arguments:
            width (int): Width of Rectangle
            height (int): Height of rectangle
            """
        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("height", height):
            self.__height = height
