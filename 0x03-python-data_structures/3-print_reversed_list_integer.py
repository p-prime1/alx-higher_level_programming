#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    "Prints integers in reversed order"
    i = len(my_list) - 1
    if i == 0:
        return '\n'
    while i >= 0:
        print("{:d}".format(my_list[i]))
        i -= 1
