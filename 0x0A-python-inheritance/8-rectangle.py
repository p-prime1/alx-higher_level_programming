#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry

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
