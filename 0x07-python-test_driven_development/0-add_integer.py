#!/usr/bin/python3
"""
add_integer module int and float
Function that adds 2 integers
"""


def add_integer(a, b=98):
    """Function that adds 2 integers
    Args:
        a (int): First integer.
        b (int): Second integer.
    Raises:
       TypeError
    Return:
        Sum of two digits int and float
    """
    if not (type(a)in (int, float)):
        raise TypeError("a must be an integer")
    if not (type(b) in (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
