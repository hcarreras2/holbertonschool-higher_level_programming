#!/usr/bin/python3

"""A function to know if isinstance"""

def is_same_class(obj, a_class):
    """Returns True if an object is exactly an instance of
    the specified class; otherwise false"""
    
    if isinstance(obj, a_class):
        return True
    else:
        return False
