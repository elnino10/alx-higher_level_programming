#!/usr/bin/python3
"""module contains from_json_string(my_str) function that returns
an object (Python data structure) represented by a JSON string
"""
import json


def from_json_string(my_str):
    """returns an object (Python data structure) represented by a JSON string

    Args:
        my_str (_json_): JSON string
    """
    return json.loads(my_str)
