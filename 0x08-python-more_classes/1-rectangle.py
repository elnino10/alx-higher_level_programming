#!/usr/bin/python3
"""The Rectangle class module

>>> rect = Rectangle(4, 10)
>>> rect.__dict__
{'_Rectangle__height': 10, '_Rectangle__width': 4}
"""


class Rectangle():
    """Rectangle module that defines a rectangle

    how to use:
    >>> Rectangle = __import__('1-rectangle').Rectangle
    >>> rect = Rectangle(2, 4)
    >>> rect.__dict__
    {'_Rectangle__height': 4, '_Rectangle__width': 2}

    >>> rect.width = 5
    >>> rect.height = 7
    >>> rect.__dict__
    {'_Rectangle__height': 7, '_Rectangle__width': 5}
    """

    def __init__(self, width=0, height=0):
        """instantiates object width values of width and height"""
        self.__height = height
        self.__width = width

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
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
