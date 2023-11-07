#!/usr/bin/python3
"""module contains load_from_json_file() function that
creates an Object from a 'JSON file'
"""
import json


def load_from_json_file(filename):
    """creates an Object from a 'JSON file'

    Args:
        filename (_type_): _description_
    """
    with open(filename, "r", encoding="utf-8") as my_file:
        return json.load(my_file)
