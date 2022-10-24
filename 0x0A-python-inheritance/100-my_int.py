#!/usr/bin/python3
7"""Class My Imteger"""


class MyInt(int):
    """Class Myint that inherits from int"""
    def __eq__(self, val):
        """what was != is now =="""
        return int(self) != val

    def __ne__(self, val):
        """what was == is now !="""
        return int(self) == val
