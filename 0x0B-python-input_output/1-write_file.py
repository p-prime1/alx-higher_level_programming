#!/usr/bin/python3

"""This module provides a function that writes to a file"""


def write_file(filename="", text=""):
    """Writes the specified text to the file

    If the file exist the content wil be overwritten,
    else a new file would be created
    Args:
        filename (str): Name of file
        text (str): Text to be written to the file

    Return:
        int: The number of characters written to the file
        """
    with open(filename, mode='w', encoding='utf-8') as file:
        return (file.write(text))
