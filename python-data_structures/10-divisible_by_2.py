#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Returns a list of all integers in the input list
    that are divisible by 2."""

    for i in my_list:
        if i % 2 == 0:
            return True
    else:
        return False
