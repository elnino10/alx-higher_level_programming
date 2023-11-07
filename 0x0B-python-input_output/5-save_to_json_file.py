#!/usr/bin/python3
"""module constains save_to_json_file() function that writes an
Object to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, _filename):
    """writes an Object to a text file, using a JSON representation

    Args:
        my_obj (_object_): object to be written
        filename (_type_): file name
    """
    with open(_filename, "w", encoding="utf-8") as my_file:
        return json.dump(my_obj, my_file)
