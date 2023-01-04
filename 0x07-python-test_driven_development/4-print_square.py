#!/usr/bin/python3

"""
Print square module
"""


def print_square(size):
    """Print a square
    Args:
        size (`int`): The size of the square.
    Raises:
        TypeError: If `size` is not an integer.
        ValuError: If `size` is < 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        if i < size - 1:
            print()
