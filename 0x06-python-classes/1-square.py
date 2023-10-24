#!/usr/bin/python3
"""A class that defines a square by private instance attribute and
instantiation with size"""


class Square:
    """A square class that defines a square"""
    __size = None

    def __init__(self, size):
        """Initializes private attribute size"""
        self.__size = size
