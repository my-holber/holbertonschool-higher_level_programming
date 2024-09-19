#!/usr/bin/python3
'''
This script defines a function to list all
attributes and methods of an object.
'''


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of strings representing the names of the object's attributes and
        methods.
        Use dir() to get a list of all attributes and methods of the object
    """
    return dir(obj)
