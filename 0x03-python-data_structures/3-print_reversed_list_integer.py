#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Prints all integer in the list in reverse order"""
    if my_list:
        for i in reversed(my_list):
            print("{:d}".format(i))
