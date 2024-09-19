#!/usr/bin/python3

""" This class defines a square"""

class Square:
    """This is the class named square"""
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
    
    def area(self):
        """Returns the current square area"""
        return self.__size ** 2
