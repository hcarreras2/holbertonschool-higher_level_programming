#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Add elements to a set of unique integers.
    """
    my_set = set()
    for i in my_list:
        my_set.add(i)
    return my_set
