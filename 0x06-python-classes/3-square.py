#!/usr/bin/python3
"""Create a class that defines a Square"""


class Square:
    """A class that defines a square"""
    __size = None

    def __init__(self, size=0):
        """Initialize class"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the area of square"""
        return (self.__size ** 2)
