#!/usr/bin/python3
"""9. Student to JSON"""


class Student:
    def __init__(self, first_name, last_name, age) -> None:
        """Initializing instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary with instance attributes"""
        return self.__dict__
