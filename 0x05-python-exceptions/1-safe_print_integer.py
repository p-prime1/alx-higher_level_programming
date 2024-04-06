#!/usr/bin/python3
def safe_print_integer(value):
    """Prints an integer"""
    try:
        print("{:d}".format(value))
    except ValueError:
        return (False)
    return (True)
