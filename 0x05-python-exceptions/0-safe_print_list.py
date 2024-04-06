#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Prints x elements in a list"""
    i = 0
    while (True):
        try:
            print(my_list[i], end="" if i <= x else "\n")
            i += 1
            if (i == x):
                break
        except IndexError:
            print("\n")
            break
    return (i)
