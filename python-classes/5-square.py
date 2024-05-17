#!/usr/bin/python3
"""Defines a square."""


class Square:
    """
    This class represents a square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square object with a specified size.

        Args:
            size (int): The size of the square.
        """
        self.size = size

    def area(self):
        """Get the current square area."""
        return (self.__size ** 2)

    @property
    def size(self):
    """Get the size of square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter of the value size.
            Args:
                value (int): Value corresponding to the size.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints in stdout the square with the character #."""
        if self.__size < 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
