#!/usr/bin/python3
"""
class MyList that inherits from list

"""


class MyList(list):
    """ Class that inherits the attributes references of class list

    Args:
        list: class list

    """

    def print_sorted(self):
        """Выводит отсортированный список (по возрастанию)."""
        print(sorted(self))
