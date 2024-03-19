#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Retrieves an element from a list at an index"""
    new_list = list()
    new_list = my_list[:]
    if (idx > (len(new_list) - 1) or idx < 0):
        return (NONE)
    j = 0
    for i in my_list:
        if j == idx:
            break
        else:
            j += 1
    new_list[j] = element
    return (new_list)
