#!/usr/bin/python3

"""class named BaseGeometry"""


class BaseGeometry:
    """raises Exception with the message:
    area() is not implemented"""

    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates a value, assumes name is always a string
        if value is not an integer raise TypeError with message:
            <name> must be integer
        if value is <= 0 raise ValueError with message:
            <name> must be greater than 0"""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        
class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry
    private instance attribute width and height
    validates width and height to be positive integers
    initializes width and height"""
    def __init__(self, width, height):
        """initializes width and height"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
