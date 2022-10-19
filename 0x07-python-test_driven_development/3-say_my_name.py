#!/usr/bin/python3
"""SayMyName module"""


def say_my_name(first_name, last_name=""):
    """
    Args: Prints My name is <first name> <last name>.
        :param last_name: <first name> (must be strings),
        :param first_name: <last name> (must be strings).

    Raises:
    TypeError - if not a string.
    """
    def say_my_name(first_name, last_name=""):
    """Prints "My name is" followed by the first name and optional last name"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name
