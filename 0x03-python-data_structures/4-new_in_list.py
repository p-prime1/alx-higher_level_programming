#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    a = len(my_list) - 1
    temp_list = my_list
    if idx > a or idx < 0:
        return temp_list
    else:
        temp_list[idx] = element
        return temp_list
