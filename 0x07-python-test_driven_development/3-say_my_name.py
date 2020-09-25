#!/usr/bin/python3
"""
say_my_name module
Function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    Function that prints My name is <first name> <last name>
    Args:
        first_name (str): First string.
        last_name (str): Second string.
    Raises:
       TypeError: If first_name or last_name are not string
    Return:
       My name is <first name> <last name>
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
