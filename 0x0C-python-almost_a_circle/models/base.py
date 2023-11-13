#!/usr/bin/python3
"""This class is the "base" of all other classes in this project
"""
import json


class Base:
    """base class of the classes for this project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """manages id attribute in all future classes and to avoid
        duplicating the same code

        Args:
            id (int, optional): identification. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list): list of dictionaries
        """
        if list_dictionaries is None or not len(list_dictionaries) > 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): list of instances who inherits of Base
        """
        my_list = []
        if list_objs is not None:
            for item in list_objs:
                my_list.append(item.to_dictionary())

        filename = f"{cls.__name__}.json"
        with open(filename, "w", encoding="utf-8") as my_file:
            my_file.write(cls.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string

        Args:
            json_string (list): string representing a list of dictionaries
        """
        my_list = []
        if json_string is not None:
            parsed_string = json.loads(json_string)
            for item in parsed_string:
                my_list.append(item)
        return my_list

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""

        inst = cls(2, 4)
        inst.update(**dictionary)
        return inst

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = f"{cls.__name__}.json"

        inst_list = []
        try:
            with open(filename, "r", encoding="utf-8") as my_file:
                list_dict = cls.from_json_string(my_file.read())
                for item in list_dict:
                    inst_list.append(cls.create(**item))
            return inst_list
        except FileNotFoundError:
            return inst_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CSV

        Args:
            list_objs (list): list of instances
        """
        list_dict = []
        if list_objs is not None:
            for item in list_objs:
                list_dict.append(item.to_dictionary())

            filename = f"{cls.__name__}.csv"
            with open(filename, "w", encoding="utf-8") as my_file:
                my_file.write(cls.to_json_string(list_dict))

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in CSV"""
        filename = f"{cls.__name__}.csv"

        my_list = []
        try:
            with open(filename, "r", encoding="utf-8") as my_file:
                list_dict = cls.from_json_string(my_file.read())
                for item in list_dict:
                    my_list.append(cls.create(**item))
                return my_list
        except FileNotFoundError:
            return []
