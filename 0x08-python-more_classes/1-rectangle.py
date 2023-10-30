#!/usr/bin/python3
"""The Rectangle class module"""


class Rectangle():
    """Rectangle module that defines a rectangle"""
    __width = None
    __height = None

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """returns the width of rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        """sets the width of rectangle"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        """returns the height of rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        """sets the height of rectangle"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = height
