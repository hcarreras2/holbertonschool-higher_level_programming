#!/usr/bin/python3
"""Define a class named Rectangle."""


class Rectangle:
    """This class represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance.

        Args:
          width (int, optional): The width of the rectangle. Defaults to 0.
          height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
          value (int): The width value.

        Raises:
          TypeError: If value is not an integer.
          ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
          value (int): The height value.

        Raises:
          TypeError: If value is not an integer.
          ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__height * self.__width

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)
