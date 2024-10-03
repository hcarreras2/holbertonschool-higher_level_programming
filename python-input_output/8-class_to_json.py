#!/usr/bin/python3

"""A function that returns the dictionary description
with a simple data structure for JSON serialization of
an object"""

import json


def class_to_json(obj):
    """Returns a dictionary description with simple data
    structure for JSON serialization of an object"""

    return obj.to_json_string()
