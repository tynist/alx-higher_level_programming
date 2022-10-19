#!/usr/bin/python3
"""Addition of Integer"""


def add_integer(a, b=98):
    """
    Args: Adds two number a and b.
        :param a: first number input,
        :param b: second number input.

    Raise: TypeError - if not an integers or floats.

    Returns: addition of a and b (an integer).
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
