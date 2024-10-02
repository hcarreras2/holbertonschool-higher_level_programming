#!/usr/bin/python3

"""Append a string to the end of a text file and
return the number of characters added"""


def append_write(filename="", text=""):
    """Append a string to the end of a text file and
        return the number of characters added.

    If the file doesn't exist, it is created.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, "a") as file:
        added_chars = file.write(text)
        return added_chars
