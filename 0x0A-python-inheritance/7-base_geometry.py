#!/usr/bin/python3
"""BaseGeometry class

# name = test area()
>>> bg = BaseGeometry()
>>> bg.area()
Traceback (most recent call last):
...
Exception: area() is not implemented
"""


class BaseGeometry:
    """BaseGeometry class with area and integer validator methods

        >>> bg = BaseGeometry()
    >>> bg.integer_validator("new", 0)
    Traceback (most recent call last):
    ...
    ValueError: new must be greater than 0
    """

    def area(self):
        """gets the area of a geometry

        keyword arguments:
        none passed

        return:
        a general exception raised
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value as an integer"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
