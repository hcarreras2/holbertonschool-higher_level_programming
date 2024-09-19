#!/usr/bin/python3

"""Class named Square that will have a private instance and instantiation"""


class Square:
    """This is the class named Square"""
    def __init__(self, size=0):
        """Size must be an integer otherwise TypeError

        Args:
            size (int): size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
