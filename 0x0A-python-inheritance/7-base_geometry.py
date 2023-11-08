#!/usr/bin/python3
"""BaseGeometry class

# name = test area()
>>> bg = BaseGeometry()
>>> bg.area() #doctest: +ELLIPSIS
Traceback (most recent call last):
...
Exception: area() is not implemented

>>> bg.integer_validator("new", (2,)) #doctest: +ELLIPSIS
Traceback (most recent call last):
...
TypeError: new must be an integer

>>> bg.integer_validator() #doctest: +ELLIPSIS
Traceback (most recent call last):
...
TypeError: BaseGeometry.integer_validator() missing 2 required \
positional arguments: 'name' and 'value'

>>> bg.integer_validator("new") #doctest: +ELLIPSIS
Traceback (most recent call last):
...
TypeError: BaseGeometry.integer_validator() missing 1 required positional argument: 'value'
"""


class BaseGeometry:
    """BaseGeometry class with area and integer validator methods

    >>> BaseGeometry = __import__('7-base_geometry').BaseGeometry
    >>> bg = BaseGeometry()
    >>> bg.integer_validator("new", 0)
    Traceback (most recent call last):
    ...
    ValueError: new must be greater than 0
    """

    def area(self):
        """gets area of geometry

        Raises:
            Exception: general exception raised
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the value argument passed

        Args:
            name (str): name of argument
            value (int): value to be validated

        Raises:
            TypeError: <name> must be an integer
            ValueError: <name> must be greater than 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
