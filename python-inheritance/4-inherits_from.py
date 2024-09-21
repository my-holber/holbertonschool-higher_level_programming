#!/usr/bin/python3
"""
This line tells the system to use Python 3 to run this script
"""


def inherits_from(obj, a_class):
    """
        Check if object if an instance of the specified inherited class.

        Arguments:
            obj (class): Class to test.
            a_class (type): Type to check obj.
        Return:
            (bool) Resultat.
    """
    return type(obj) is not a_class
