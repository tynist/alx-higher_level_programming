#!/usr/bin/python3
"""Class inherits_from"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of class
    inherited; otherise False
    """
    if isinstance(obj, a_class) and \
       issubclass(a_class, obj.__class__) is False:
           return True
    return False
