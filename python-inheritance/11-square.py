#!/usr/bin/python3

"""Square class that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle
"""Import from Rectangle.py"""


class Square(Rectangle):
    """Square class that inherits from Rectangle"""
    def __init__(self, size):
        """Initialize a new Square instance"""
        self.__size = size
        super().__init__(size, size)
        self.integer_validator("size", size)

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Return a string representation of the square"""
        return "[Square] " + super().__str__()
