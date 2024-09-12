#usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Prints the x elements of a given list.
    x can be bigger than the lenght of my_list
    x represents the number of elements to print
    returns the real number of elements printed"""
    for x in my_list:
        print(x)
    if x >= my_list:
        return x
