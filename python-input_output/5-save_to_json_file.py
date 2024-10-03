#!/usr/bin/python3

"""A function that writes an Object to a text file,
using a JSON representation"""


import json


def save_to_json_file(my_obj, filename):
    """Saves an object to a JSON file
    Args:
    my_obj (object): The object to be saved
    filename (str): The name of the file to save to
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
        return
