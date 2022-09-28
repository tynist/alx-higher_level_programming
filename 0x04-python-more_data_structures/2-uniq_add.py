#!/usr/bin/python3
def uniq_add(my_list=[]):
    """adds all unique integers in a list only once for each integer."""
    the_list = set(my_list)
    nums = 0

    for i in the_list:
        nums += i
    return nums
