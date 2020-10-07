#!/usr/bin/python3
"""
Returns the number of lines of a text file
"""


def number_of_lines(filename=""):
    """
    Returns the number of lines of a text file
    """
    with open(filename, encoding="utf-8") as m_file:
        l_num = 0
        for line in m_file:
            l_num += 1
        return l_num
