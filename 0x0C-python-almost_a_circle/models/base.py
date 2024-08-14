#!/usr/bin/python3

'''Module contains the class Base'''


class Base:
    '''Class named Base 
    Private class attribute: __nb_objects, avoids duplication of id for all 
    child classes
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the class with the public instance attribute id
        
        Assigns the __nb_objects to id if no arguments was provided

        Args:
            id (int): Tracks the id for all child class
        """
        if id == None:
           Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
