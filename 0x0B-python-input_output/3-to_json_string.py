#!/usr/bin/python3
"""module contains to_json_string() function that returns the JSON
representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)

    Args:
        my_obj (_object_): object string
    """
    return json.dumps(my_obj)
