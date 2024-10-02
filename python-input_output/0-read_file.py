#!/usr/bin/python3
"""A function that reads a file"""

def read_file(filename=""):
    """
    Reads a file and prints output to stdout
    """
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end="")
