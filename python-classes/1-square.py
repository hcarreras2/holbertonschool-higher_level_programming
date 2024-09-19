#!/usr/bin/python3

"""Class named Square that will have a private instance and instantiation"""


class Square:
    """This is the class named Square"""
    def __init__(self, size):
        """This is the instantiation of the class

        Args:
            size (int): The size of the square
        """
        self.__size = size
