#!/usr/bin/python3

"""A function thhat returns an object in Python
represented by a JSON string"""


import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string"""
    return json.loads(my_str)
