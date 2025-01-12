#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle.

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (any): The symbol used for string representation.
    """
    number_of_instances = 0
    print_symbol = '#'
    def __init__(self, width=0, height=0):
        """Initializes private class attributes
            width (int): The width of the Rectangle
            height (int): The height of the Rectangle
            number_of_instances (int): Counts the number og the instances
            """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Returns the width variable"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Sets the value of the width"""
        if value is not int:
            raise TypeError("width must be >= 0")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the value of the height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Sets the value of the Height"""
        if value is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def perimeter(self):
        """Returns the perimeter of the Rectangle"""
        if self.__height == 0 or self.__width == 0:
            return (0);
        return (self.__height + self.__width)

    def area(self):
        """Returns the Area fo the rectangle"""
        return (self.__height * self.__width)

    def __del__(self):
        """Prints a message when an instance is deleted"""
        return (f"Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area > rect_2.area or rect_1.area == rect_2.area:
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width, height and size all equal"""
        width = size
        height = size
        return cls(width, height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
