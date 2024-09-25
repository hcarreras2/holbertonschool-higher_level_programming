#!/usr/bin/python3

"""Function to check if obj is an instance of a class
that inherited directly or indirectly from the class"""


def inherits_from(obj, a_class):
    """Check if obj is an instance of a class that inherited
    directly or indirectly from the class

    Returns:
    bool: True if obj is an instance of a class that inherited
    directly or indirectly from the class, False otherwise
    """

    if issubclass(obj, a_class):
        return True
    else:
        return False
