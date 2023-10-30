#!/usr/bin/python3
"""The Rectangle class module"""


class Rectangle():
    """Rectangle module that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """instantiates object width values of width and height"""
        self.__width = width
        self.__height = height

    def __str__(self):
        """returns unofficial representation of the rectangle with
        the character #
        """
        return "{}".format(
            ("#" * self.__width)) + "".join(
                ["\n" + "#" * self.__width] * (self.__height - 1)) if not (
                self.__height == 0 or self.__width == 0) else ""

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

    def area(self):
        """returns the rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * self.__height) + (2 * self.__width)
