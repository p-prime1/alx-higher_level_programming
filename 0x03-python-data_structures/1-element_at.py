#!/usr/bin/python3
def element_at(my_list, idx):
    """Retrieves an element from a list at an index"""
    if (idx > (len(my_list) - 1) or idx < 0):
        return (NONE)
    j = 0
    for i in my_list:
        if j == idx:
            break
        else:
            j += 1
    return (my_list[j])
