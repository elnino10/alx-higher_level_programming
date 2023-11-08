#!/usr/bin/python3
"""module has add_attribute() function that adds a new
attribute to an object if it's possible
"""


def add_attribute(obj, name, value=""):
    """adds a new attribute to an object if possible

    Args:
        obj (type): object to which attribute is to be added
        name (any): attribute to be added to object
        value (any): value of the attribute
    """
    if hasattr(obj, "__dict__"):
        obj.__dict__[name] = value
    else:
        raise TypeError("can't add new attribute")
