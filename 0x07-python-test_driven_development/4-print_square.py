#!/usr/bin/python3
"""
print_square module
Function that prints a square with the character #.
"""


def print_square(size):
    """
    Function that prints a square with the character #.
    Args:
        size (int): First integer.
    Raises:
       TypeError: If size are not int
    Return:
       A square.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        print("#" * size)
