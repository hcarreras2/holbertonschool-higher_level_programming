#!/usr/bin/python3

"""Class named VerboseList that extend list class"""


class VerboseList(list):
    """Class that extend list class
    prints a notification message every time an item is added
    or removed"""

    def append(self, item):
        """append method that print a notification message"""
        super().append(item)
        print("Added [{}] to the list".format(item))

    def extend(self, item):
        """extend method that print a notification message with
        numbers of items added"""
        super().extend(item)
        print("Extended the list with [{}] items".format(len(item)))

    def remove(self, item):
        """
        Before removing the item from the list,
        print a message like “Removed [item] from the list.”
        """
        super().remove(item)
        print("Removed [{}] from the list".format(item))

    def pop(self, index):
        """
        Before popping the item from the list,
        print a message like “Popped [item] from the list.”
        If the index is not specified, default behavior
        is to pop the last item.
        """
        super().pop(index)
        print("Popped [{}] from the list".format(item))
