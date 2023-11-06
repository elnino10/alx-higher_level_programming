#!/usr/bin/python3

def is_same_class(obj, a_class):
    """returns True if the object is exactly an instance of the specified
    class ; otherwise False
    """
    if type(obj).__name__ == a_class.__name__:
        return True
    return False
