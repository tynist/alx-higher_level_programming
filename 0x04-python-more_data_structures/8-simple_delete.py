#!/usr/bin/python3
def simple_delete(a_dict, key=""):
    """Deletes a key in a dictionary."""
    a_dict.pop(key, None)
    return a_dict
