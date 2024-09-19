#!/usr/bin/python3
"""
This line tells the system to use Python 3 to run this script
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or if it is an instance of a class
    that inherited from, the specified class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a_class or
        a subclass of a_class, otherwise False.
    """
    return isinstance(obj, a_class)
