#!/usr/bin/python3
"""add_integer function returns the sum of two integers

works for two integers
>>> add_integer(2, 2)
4
"""


def add_integer(a, b=98):
    """returns sum of two intergers
    numbers must be casted to integers before adding

    >>> add_integer(-1, -2)
    -3
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(a)


    return a + b
