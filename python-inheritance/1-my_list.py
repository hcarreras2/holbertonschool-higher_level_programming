#!/usr/bin/python3

"""Class named Mylist that inherits form list"""
class MyList(list):
    """Class that inherits from list"""


    def print_sorted(self):
        """Method that prints the list in sorted order
    (ascending sort)"""
        print(sorted(self))
