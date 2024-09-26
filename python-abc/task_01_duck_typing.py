#!/usr/bin/python3
from abc import ABC
from abc import abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass




class Circle(Shape):

    def area(self):
        pass


    def perimeter(self):
        pass



class Rectangle(Shape):
    def __init__(self) -> None:
        super().__init__()

    def area(self):
        pass


    def perimeter(self):
        pass