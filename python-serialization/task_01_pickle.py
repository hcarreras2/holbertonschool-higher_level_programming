#!/usr/bin/python3

import pickle

"""Custom class named CustomObject that has student attributes"""


class CustomObject:
    """Custom class with student attributes"""


    def __init__(self, name, age, is_student):
        """Initialize CustomObject with name, age, and is_student
        Args:
        name (str): student name
        age (int): student age
        is_student (bool): whether the person is a student
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print out CustomObject attributes"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return None
        except Exception as e:
            return None
    
