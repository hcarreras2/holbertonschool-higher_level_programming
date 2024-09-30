#!/bin/usr/python3
"""Abstract class named Animal"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class Animal"""

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """Subclass Dog"""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Subclass Cat"""

    def sound(self):
        return "Meow"
