#!/usr/bin/python3
def no_c(my_string):
    "Removes the letters 'c' and 'C'"
    my_string = [i for i in my_string if i != 'c' and i != 'C']
    return ''.join(my_string)
