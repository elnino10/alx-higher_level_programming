#!/usr/bin/python3
"""function that returns the dictionary description with simple
data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""
import json


def class_to_json(obj):
    """that returns the dictionary description with simple data structure

    Args:
        obj (_class_): instance of a Class
    """
    with open(obj, "r", encoding="utf-8") as _json:
        return json.dumps(_json.read())
