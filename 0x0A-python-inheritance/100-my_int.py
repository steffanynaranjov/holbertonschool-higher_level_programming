#!/usr/bin/python3
"""
MyInt module
"""


class MyInt(int):
    """subclass MyInt from class int"""
    def __equal__(self, other):
        """Compare equal or  different to other"""
        return (int(self) != int(other))

    def __diff__(self, other):
        """Compare equal or different to other"""
        return (int(self) == int(other))
