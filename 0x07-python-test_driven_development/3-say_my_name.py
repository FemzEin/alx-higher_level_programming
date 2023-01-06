#!/usr/bin/python

"""
Say my name module
"""


def say_my_name(first_name, last_name=""):
    """Prints the name
    Args:
        first_name (:obj:`str`): The first name
        last_name (:obj: `str`, optional): The last name
    Raises:
        TypeError: If `first_name` or `last_name` is not a ``str``.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
