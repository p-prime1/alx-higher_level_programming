#!/usr/bin/python3

'''Module contains the Rectangle class'''

Base = __import__('base').Base


class Rectangle(Base):
    '''Rectangle class, Inherits from Base class in the base module'''

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialzes both the Parents function (Base) and the Rectangle
        function

        Args:
            Private instance atrribute - width (int): Defines the width of
            the Rectangle.
            Private instance attribute - height (int): Defines the height
            of the rectangle
            Private instance attribute - x (int)
            Private instance attribute - y (int)
        """
        if not (isinstance(width, int) or isinstance(width, float)):
            raise TypeError('width must be an integer')
        if not (isinstance(height, int) or isinstance(height, float)):
            raise TypeError('height must be an integer')
        if not (isinstance(x, int) or isinstance(x, float)):
            raise TypeError('x must be an integer')
        if not (isinstance(y, int) or isinstance(y, float)):
            raise TypeError('y must be an integer')
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @getter
    def get_width(self):
        """Returns the value for the width"""
        return (self.__width)

    @width.setter
    def set_width(self):
        """Sets the value for width"""
        self.__width = width

    @getter
    def get_height(self):
        """Returns the value of height"""
        return (self.__height)

    @height.setter
    def set_height(self):
        """Sets the value for the heitght"""
        self.__height = height

    @getter
    def get_x(self):
        """Returns the value of x"""
        return (self.__x)

    @x.setter
    def set_x(self):
        """Sets the value of x"""
        self.__x = x

    @getter
    def get_y(self):
        """Returns the value of y"""
        return (self.__y)

    @y.setter
    def set_y(self):
        """Sets the value of y"""
        self.__y = y
