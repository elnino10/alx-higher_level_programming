#!/usr/bin/python3
"""Square class module"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """__init__ method
        Args:
            size (int): size of the square
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Area of a square"""
        return self.__size ** 2
