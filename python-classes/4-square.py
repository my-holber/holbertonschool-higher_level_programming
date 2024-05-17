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
        return (self.__size ** 2)

    @property
    def size(self):
        """Get the size of square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter of the size field."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
