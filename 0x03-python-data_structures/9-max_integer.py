#!/usr/bin/python3
def max_integer(my_list=[]):
    "Function that finds the biggest integer of a list"
    a = len(my_list) - 1
    if a < 0:
        return None
    i = 0
    j = my_list[i]
    while i <= a:
        if my_list[i] > j:
            j = my_list[i]
        else:
            i += 1
    return j
