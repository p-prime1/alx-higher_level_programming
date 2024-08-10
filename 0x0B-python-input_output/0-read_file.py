#!/usr/bin/python3

"""Function reads from a file"""


def read_file(filename=""):
    """Arguments:
        filename (file): Name of file
        """
    with open(filename, encoding='utf-8') as file:
        print(file.read().rstrip())
