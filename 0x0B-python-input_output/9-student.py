#!/usr/bin/python3

"""Module contains the Student class"""


class Student:
    """The class student, has three public attributes"""

    def __init__(self, firstname, lastname, age):
        """Methods initializes the class with the arguments
        Args:
            firstname (str): Firstname of the Student
            lastname (str): Lastname of the student
            age (int): Age of the student
        """
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def to_json(self):
        """Method returns the dictionary representation of an
        instance of the Studemts"""
        return (self.__dict__)
