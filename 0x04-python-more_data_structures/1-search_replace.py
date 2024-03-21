#!/usr/bin/python3
import copy


def search_replace(my_list, search, replace):
    """Searches and replaces an element in a copy of a list"""
    new_list = copy.deepcopy(my_list)
    for i in range(len(new_list)):
        if (new_list[i] == search):
            new_list[i] = replace
    return (new_list)
