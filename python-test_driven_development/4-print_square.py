#!/usr/bin/python3
"""

 function that prints a square with the character #
"""


def print_square(size):
    """ Function that prints a square with the character #

    Args:
        size: size of the square printed

    Returns:
        No return

    Raises:
        TypeError: If size is not an integer number


    """
    if not isinstance(size, (int)):
        raise TypeError("size must be an integer")
    if not isinstance(size, (float)) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print(size * "#")
