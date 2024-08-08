#!/usr/bin/python3

"""Defines a geometry class"""


class BaseGeometry:

    def integer_validator(self, name, value):
        """Validates value if its an integer
        Arguments:
            name (String): Name
            value (int): Integer to be validated
            """
        if type(value) is not int:
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
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area"""
        return (self.__width * self.__height)


    def __str__(self):
        """Returns a formal String"""
        return (f"[Rectangle] {self.__width}/{self.__height}")

