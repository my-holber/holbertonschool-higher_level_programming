#!/usr/bin/python3
"""
This is class Square that defines a square
"""


class Square():
    """
    Return: a empty class square
    """
    def __init__(self, size) -> None:
        self.__size = size
        

















my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)
