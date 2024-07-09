#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Prints x elements in a list"""
    i = 0
    try:
        while (i < x):
            print(my_list[i], end='')
            i += 1
    except IndexError:
        pass
    except TypeError:
        pass
    except NameError:
        pass
    print()
    return (i)
