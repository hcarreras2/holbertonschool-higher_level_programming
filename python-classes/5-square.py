#!/usr/bin/python3

"""This is a class named square"""


class Square:
    """This is a class named square"""
    def __init__(self, size=0):
        """This is a constructor method

        Args:
        size (int): The size of the square
        """
        self.__size = size

    @property
    def size(self):
        """This is a getter method for size
        Returns:
        int: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """This is a method to set the size of the square
        Args:
        value (int): size of the square.

        Raises:
        TypeError: If the size is not an integer
        ValueError: If the size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This is a method to calculate the area of the square

        Returns:
        int: The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """This is a method to print in stdout the square
        with the character #

        If i is = 0 print empty line
        """
        for i in range(self.__size):
            print("#" * self.size)
        if self.size == 0:
            print("")
