#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """This function takes a dictionary as an argument and returns a new dictionary
    where each value is multiplied by 2."""
    new_dict = {}
    for key, value in a_dictionary.items():
        new_dict[key] = value * 2
        return new_dict
