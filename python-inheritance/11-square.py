#!/usr/bin/python3
"""
    Class file for Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        Initialize a square.
        Arguments:
        size (int): The size of the square side.
    """
    def __init__(self, size):
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
         return f"[Square] {self.__size}/{self.__size}"
