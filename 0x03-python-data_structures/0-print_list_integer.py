#!/usr/bin/python3
def print_list_integer(my_list=[]):
    "Prints all integers in of list"
    a = len(my_list) - 1
    i = 0
    while i != a:
        print("{}".format(my_list[i]))
        i += 1
