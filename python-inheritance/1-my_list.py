#!/usr/bin/python3
'''
This script defines a class MyList that extends
the built-in list class.
'''


class MyList(list):
    """
    A subclass of list with an additional method to print the list sorted in
    ascending order.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending order.
        """
        print(sorted(self))
