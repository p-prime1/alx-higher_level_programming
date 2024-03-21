#!/usr/bin/python3


def uniq_add(my_list=[]):
    """Adds all the unique elements in a list"""
    new_set = set()
    for i in my_list:
        new_set.add(i)
    j = 0
    for i in new_set:
        j += i
    return (j)
