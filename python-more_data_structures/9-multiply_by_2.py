#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """This function takes a dictionary as an
    argument and returns a new dictionary
    where each value is multiplied by 2."""
    new_dict = {}
    for new_dict in a_dictionary:
        new_dict = a_dictionary[new_dict] * 2
    return new_dict
