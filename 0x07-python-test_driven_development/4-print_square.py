#!/usr/bin/python3
"""print_square function prints a square with the character #

>>> print_square(2)
##
##
"""


def print_square(size):
    """prints a square with the character #

    parameter: size
    """
    if size or size == 0:
        if isinstance(size, str):
            raise TypeError("size must be an integer")

        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")

        if isinstance(size, float):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
    else:
        raise TypeError("size must be an integer")
