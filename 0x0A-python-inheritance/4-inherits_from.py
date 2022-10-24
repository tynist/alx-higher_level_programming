#!/usr/bin/python3
"""Class inherits_from""


def is_kind_of_class(obj, a_class):
    """
    contains the MyList class
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
