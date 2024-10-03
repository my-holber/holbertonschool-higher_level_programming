#!/usr/bin/python3
'''10. Student to JSON with filter'''


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        eturns a dictionary with attributes of the Student object.
        If a list of attrs strings is passed,
        only those attributes whose names are
        specified in this list are returned.
        If attrs is not passed, all attributes of the object are returned.
        '''

        if attrs is None:
            return self.__dict__

        new_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                new_dict[attr] = getattr(self, attr)
        return new_dict
