#!/usr/bin/python3

def best_score(a_dictionary):
    """Returns a key with the biggest integer if it exists in the
    dictionary,otherwise None"""
    if a_dictionary and a_dictionary.values():
        return max(a_dictionary, key=a_dictionary.get)
    else:
        return None
