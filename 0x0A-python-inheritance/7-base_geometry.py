#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class with area and integer validator methods"""

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
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
