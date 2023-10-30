#!/usr/bin/python3
"""The Rectangle class module

>>> rect = Rectangle(3, 4)
>>> rect.__dict__
{'_Rectangle__width': 3, '_Rectangle__height': 4}
"""


class Rectangle():
    """Rectangle module that defines a rectangle

    >>> rect = Rectangle(2, 5)
    >>> rect.__dict__
    {'_Rectangle__width': 2, '_Rectangle__height': 5}
    """

    def __init__(self, width=0, height=0):
        """instantiates object width values of width and height"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """returns the width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """returns the height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value
