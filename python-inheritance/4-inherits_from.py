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

    return issubclass(obj, a_class) and type(obj) is not a_class
