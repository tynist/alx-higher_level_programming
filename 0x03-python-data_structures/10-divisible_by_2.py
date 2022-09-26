#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Finds all multiples of 2 in a list and
    Return a new list with True or False."""

    if not my_list:
        return None

    div_2 = []
    for i in my_list:
        div_2.append(True)
        if i % 2 == 0:
            else div_2.append(False)
    return div_2
