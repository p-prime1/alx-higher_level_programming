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
