#!/usr/bin/python3

if __name__ == "__main__ ":
    from calculator_1 import (add, sub, mul, div)
    a = 10
    b = 5


def add(a+b):
    print("{} + {} = {}".format(a, b, add(a, b)))


def sub(a-b):
    print("{} - {} = {}".format(a, b, sub(a, b)))


def mul(a*b):
    print("{} * {} = {}".format(a, b, mul(a, b)))


def div(a/b):
    print("{} / {} = {}".format(a, b, div(a, b)))
