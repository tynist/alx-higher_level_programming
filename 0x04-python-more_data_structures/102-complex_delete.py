#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """Deletes keys with a specific value in a dictionary."""
    dict_items = a_dictionary.copy()
    for i, j in dict.items():
        if value == j:
            a_dictionary.pop(i)
    return a_dictionary
