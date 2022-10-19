#!/usr/bin/python3


def print_square(size):
    """
    Args: Prints a square with the character '#'
        :param size: length of the square (must be and integer).

    Raises:
        TypeError - if size is not an integer, is a float and < 0,
        ValueError - if size < 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(0, size):
        for j in range(size):
            print("#", end="")
        print("")
