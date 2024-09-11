#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Prints all integers in the list, in reverse order."""
    if not my_list:
        return
    for i in reversed(my_list):
        print("{:d}".format(i))
