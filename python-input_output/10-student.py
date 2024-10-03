#!/usr/bin/python3
'''10. Student to JSON with filter'''


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        Возвращает словарь с атрибутами объекта Student.
        Если передан список строк attrs, то возвращаются только те атрибуты, имена которых указаны в этом списке.
        Если attrs не передан, возвращаются все атрибуты объекта.
        '''
        if attrs is None:
            # Возвращаем все атрибуты объекта в виде словаря
            return self.__dict__
        
        new_dict = {}
        # Перебираем переданные атрибуты
        for attr in attrs:
            # Проверяем, существует ли атрибут у объекта
            if hasattr(self, attr):
                # Получаем значение атрибута с помощью getattr и добавляем в новый словарь
                new_dict[attr] = getattr(self, attr)
        return new_dict