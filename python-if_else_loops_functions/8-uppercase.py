#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if char <= 'a' and <= 'z':
            uppercase_char = chr(ord(char)-32)
            print(uppercase_char, end='')
        else:
            print(char, end="")
