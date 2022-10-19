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
    names = [first_name, last_name]

    if all(type(i) is str for i in names):
        print("My name is {} {}".format(first name, last_name))

    elif isinstance(first_name, str) is False:
        raise TypeError("first name must be a string")

    elif isinstance(last_name, str) is False:
        raise TypeError("last name must be a string")
