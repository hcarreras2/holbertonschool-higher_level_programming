#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x elements of a given list of integers.
    The list may contain strings and they must be silently ignored.
    The function should be safe by avoiding any TypeError.
    Args:
    my_list (list): The list of integers to print.
    x (int): The number of elements to print.
    Returns:
    None
    """
    numbers = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            numbers += 1
        except (ValueError, IndexError):
            continue
    print()
    return numbers
