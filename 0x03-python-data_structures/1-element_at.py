#!/usr/bin/python3
def element_at(my_list, idx):
    "Retrieves an element from a list"
    a = len(my_list) - 1
    if idx > a or idx < 0:
        return "None"
    else:
        return my_list[idx]
