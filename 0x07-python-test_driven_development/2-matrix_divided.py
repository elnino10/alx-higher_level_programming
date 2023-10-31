#!/usr/bin/python3
"""the matrix_divided function receives a matrix("matrix") as its
first argument and a number("div") as the second argument. The
elements of "matrix" are divided by "div"
"matrix" must be be a list containing lists
Each row of the matrix must have the same size
Each element must be a number

>>> matrix = [[2,3,4],[6,8,10]]
>>> matrix_divided(matrix, 3)
[[0.67, 1.0, 1.33], [2.0, 2.67, 3.33]]
"""


def matrix_divided(matrix, div):
    """returns the value of matrix divided by div

    parameters: matrix and div
    raises exceptions if requirements not met
    """
    if div == 0:
        raise ZeroDivisionError('division by zero')

    if not (isinstance(div, (int, float))):
        raise TypeError('div must be a number')

    if not (isinstance(matrix, list) and
            all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')

    if len(matrix) == 0:
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')

    row_len = len(matrix[0])
    if not (all(len(row) == row_len for row in matrix)):
        raise TypeError('Each row of the matrix must have the same size')

    if not all(isinstance(el, (int, float)) for row in matrix for el in row):
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')

    return [[round(el / div, 2) for el in row] for row in matrix]
