#!/usr/bin/python3
"""
Appends a string at the end of a text file (UTF8)
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8)
    """
    with open(filename, mode="a", encoding="utf-8") as m_file:
        char = m_file.write(text)
        return char
