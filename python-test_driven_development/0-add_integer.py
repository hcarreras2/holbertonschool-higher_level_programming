#!/usr/bin/python3

""" A function that adds two values"""

def add_integer(a, b=98):
    """Adds two integers or floats (a) and (b). 
    Args:
    a (int or float): The first number to add.
    b (int or float): The second number to add. Defaults to 98.
    
    Returns:
    int: The sum of a and b.

    Raises:
    TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or a float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or a float")
    return a + b
