#!/usr/bin/python3
from abc import ABC
from abc import abstractmethod


class Animal(ABC):
    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def sound(self):
        raise TypeError(" Can't instantiate abstract class Animal with abstract method sound")



class Dog(Animal):
    def __init__(self) -> None:
        super().__init__()


    def sound(self):
        return "Bark" 


class Cat(Animal):
    def __init__(self) -> None:
        super().__init__()

    def sound(self):
        return "Meow"  




bobby = Dog()
garfield = Cat()

print(bobby.sound())
print(garfield.sound())

animal = Animal()
print(animal.sound())