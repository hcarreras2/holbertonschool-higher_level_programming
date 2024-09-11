#!/usr/bin/python3

def no_c(my_string):
    """Returns a string with all 'c' and 'C'
    characters removed from the input string"""
    result = ""
    for char in my_string:
        if char not in ['c', 'C']:
            result += char
    return result
