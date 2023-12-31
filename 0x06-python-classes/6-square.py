#!/usr/bin/python3
"""Create a class that defines a Square"""


class Square:
    """A class that defines a square"""
    __size = None
    __position = None

    def __init__(self, size=0, position=(0, 0)):
        """Initialize class"""
        self.__size = size
        if isinstance(position, tuple) and len(position) == 2 and\
            isinstance(position[0], int) and isinstance(position[1], int) and\
                position[0] >= 0 and position[1] >= 0:
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def __str__(self):
        return ""

    @property
    def size(self):
        """get the size"""
        return self.__size

    @size.setter
    def size(self, size):
        """sets the size of the square instance"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the area of square"""
        return (self.__size ** 2)

    def my_print(self):
        """prints the square in character #"""
        if self.__size == 0:
            print()
        else:
            print("{}".format("\n" * self.__position[1]), end="")
            print("{}".format("\n".join(
                [" " * self.__position[0] + "#" * self.__size] * self.__size)))

    @property
    def position(self):
        """Gets the position of the square.

        Returns:
            Position of the Square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square

        Args:
            value: value to set the position
        """
        if isinstance(value, tuple) and len(value) == 2 and\
            isinstance(value[0], int) and isinstance(value[1], int) and\
                value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
