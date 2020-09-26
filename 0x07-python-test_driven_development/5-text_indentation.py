#!/usr/bin/python3
"""
text_indentation module
Function that prints a text with 2 new lines after some characters.
"""


def text_indentation(text):
    """
    Function prints a text with 2 new lines after each of these
    characters: ., ? and :.
    Args:
        text (str): First char.
    Raises:
       TypeError: If text are not a string
    Return:
       New text change.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')
    print("\n".join([line.strip() for line in text.split("\n")]), end="")
