#!/usr/bin/python3

"""Abstract class Shape"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class Shape"""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Circle subclass from Shape"""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14 * self.radius


class Rectangle(Shape):
    """Rectangle subclass that inherits from Shape"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(Shape):
    """Prints the area and perimeter of the shape"""

    print("Area: {}".format(Shape.area()))
    print("Perimeter: {}".format(Shape.perimeter()))
