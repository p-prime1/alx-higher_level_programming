#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Retrieves an element from a list at an index"""
    if (idx > (len(my_list) - 1) or idx < 0):
        return (NONE)
    j = 0;
    for i in my_list:
        if j == idx:
            break
        else:
            j += 1
    my_list[j] = element
    return (my_list)
