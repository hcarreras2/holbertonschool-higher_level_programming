#!/usr/bin/python3

"""
A module that provides a function to write a string to a text file
and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file and return the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, 'w') as f:
        f.write(text)
        return len(text)
