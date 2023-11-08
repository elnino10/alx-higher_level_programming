#!/usr/bin/python3
"""module of a class Student that defines a student by
"""


class Student:
    """class defines a student"""

    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age

        Args:
            first_name (str): student's first name
            last_name (str): student's last name
            age (int): age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if isinstance(attrs, list):
            _dict = {}
            for el in attrs:
                if isinstance(el, str) and el in self.__dict__:
                    _dict[el] = self.__dict__[el]
            return _dict
        return self.__dict__
