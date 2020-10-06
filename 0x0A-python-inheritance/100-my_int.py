#!/usr/bin/python3
"""
Module My Int
"""


class MyInt(int):
    """This is a subclass from class int"""
    def __equal__(self, other):
        """Compare if is equal or different to other"""
        return (int(self) != int(other))

    def __different__(self, other):
        """Compare if is  equal or different to other"""
        return (int(self) == int(other))
