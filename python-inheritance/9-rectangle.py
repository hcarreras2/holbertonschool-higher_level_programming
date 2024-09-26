#!/usr/bin/python3
"""Define a class that inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Import the BaseGeometry class from the 7-base_geometry module"""


class Rectangle(BaseGeometry):
    """Class that inherits from BaseGeometry.

    Args:
        BaseGeometry (class): class defined in 5-base_geometry.py.
    """

    def __init__(self, width, height):
        """_summary_

        Args:
            width (_type_): _description_
            height (_type_): _description_
        """
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the rectangle
        [Rectangle] <width>/<height> """
        return f"[Rectangle] {self.__width}/{self.__height}"
