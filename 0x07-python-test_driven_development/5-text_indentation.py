#!/usr/bin/python3

"""
Text indentation module
"""


def text_indentation(text):
    """Prints a text with identation.
    Args:
        text (:obj: `str`): The text to print.
    Raises:
        TypeError: If `text` is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for c in text:
        print(c, end='')
        if c in ('.', '?', ':'):
            print("\n")
