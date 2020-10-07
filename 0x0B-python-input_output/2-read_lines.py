#!/usr/bin/python3
"""
Reads n lines of a text file (UTF8)
"""


def read_lines(filename="", nb_lines=0):
    """
    Reads n lines of a text file (UTF8)
    """
    with open(filename, encoding="utf-8") as m_file:
        l_num = 0
        for line in m_file:
            l_num += 1
        m_file.seek(0)
        if (l_num <= nb_lines) or (nb_lines <= 0):
            print(m_file.read(), end="")
        else:
            l_num = 0
            while l_num < nb_lines:
                print(m_file.readline(), end="")
                l_num += 1
