#!/usr/bin/python3

"""A function that checks if isinstance"""


def is_kind_of_class(obj, a_class):
    """Returns True if isinstance of class or subclass,
    otherwise False"""

    if isinstance(obj, a_class):
        return True
    else:
        return False
