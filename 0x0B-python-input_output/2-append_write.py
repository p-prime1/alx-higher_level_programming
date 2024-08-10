#!/usr/bin/python3

"""This module provides a function that writes to a file"""


def append_write(filename="", text=""):
    """Writes the specified text to the file

    If the file exist the text would be appended to the end of the file,
    else a new file would be created
    Args:
        filename (str): Name of file
        text (str): Text to be written to the file

    Return:
        int: The number of characters written to the file
        """
    with open(filename, mode='a', encoding='utf-8') as file:
        return (file.write(text))
