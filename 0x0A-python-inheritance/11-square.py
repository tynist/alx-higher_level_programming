#!/usr/bin/python3
"""A class Square that inherits Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square"""


    def __init__(self, size):
        """
        Imitializimg the Square

        Args:
            size: size of square (positive int)
        """
        self.integer_validator(size, size)
        super().__init__(size, size)
        self.__size = size
