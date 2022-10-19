#!/usr/bin/python3


def print_square(size):
    """
    Args: Prints a square with the character '#'
        :param size: length of the square (must be and integer).

    Raises:
        TypeError - if size is not an integer, is a float and < 0,
        ValueError - if size < 0.
    """
    def print_square(size):
    """prints a square with "#"'s that has a length of size """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
