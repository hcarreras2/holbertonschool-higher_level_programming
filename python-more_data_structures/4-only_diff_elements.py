#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """Return a set of elements that are in set_1 but not in set_2
    and viceversa"""
    return set_1.symmetric_difference(set_2)
