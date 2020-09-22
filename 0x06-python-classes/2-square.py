#!/usr/bin/python3
"""This is a class Square defined by size."""


class Square:
    """Def"""
    def __init__(self, size=0):
         """The initialization method of the square class
        Args:
            size (int): Is the type int private attribute
        Raise:
         TypeError: If size is not an integer
         ValueError: If size is less than 0
         """
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")

        if self.__size < 0:
            raise ValueError("size must be >= 0")
