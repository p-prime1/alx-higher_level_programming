#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    "Replaces an element of a list at a specific position"
    a = len(my_list) - 1
    if idx > a or idx < 0:
        return my_list
    else:
        my_list[idx] = element
        return my_list
