#!/usr/bin/python3

def best_score(a_dictionary):
    """Returns the biggest integer if it exists in the dictionary,
    otherwise None"""
    if a_dictionary is None:
        return None
    return max(a_dictionary.values()) if a_dictionary else None
