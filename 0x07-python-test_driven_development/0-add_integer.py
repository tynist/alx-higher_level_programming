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
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
