#!/usr/bin/python3
"""
    Определяет прямоугольник
"""


class Rectangle:
    """
    Класс прямоугольника
    """

    def __init__(self, width=0, height=0):
        """Инициализация прямоугольника"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Геттер ширины прямоугольника"""
        return self.__width

    @width.setter
    def width(self, value):
        """Сеттер ширины прямоугольника"""
        if type(value) != int:
            raise TypeError("ширина должна быть целым числом")
        if value < 0:
            raise ValueError("ширина должна быть >= 0")
        self.__width = value

    @property
    def height(self):
        """Геттер высоты прямоугольника"""
        return self.__height

    @height.setter
    def height(self, value):
        """Сеттер высоты прямоугольника"""
        if type(value) != int:
            raise TypeError("высота должна быть целым числом")
        if value < 0:
            raise ValueError("высота должна быть >= 0")
        self.__height = value
