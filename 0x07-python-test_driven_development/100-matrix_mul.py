#!/usr/bin/python3
"""100-matrix_mul module with a function matrix_mul() that
multiplies two matrices

number of rows of matrix_1 should be equal to the number of columns of matrix_2
>>> matrix_mul([[1, 2]], [[3, 4], [5, 6]])
[[13, 16]]
"""


def matrix_mul(m_a, m_b):
    """multiplies two matrices m_a and m_b

    works with floats and integers
    >>> matrix_mul([[1, 2], [4, 2.7]], [[3, 4], [3.4, 6]])
    [[9.8, 16], [21.18, 32.2]]

    >>> matrix_mul([[1, 2], [4, 2], [7, 8]], [[4, 2], [3, 6]])
    [[10, 14], [22, 20], [52, 62]]
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or all(len(row) == 0 for row in m_a):
        raise TypeError("m_a can't be empty")

    if len(m_b) == 0 or all(len(row) == 0 for row in m_b):
        raise TypeError("m_b can't be empty")

    if not all(isinstance(el, (int, float)) for row in m_a for el in row):
        raise TypeError("m_a should contain only integers or floats")

    if not all(isinstance(el, (int, float)) for row in m_b for el in row):
        raise TypeError("m_b should contain only integers or floats")

    row_len_a = len(m_a[0])
    for row in m_a:
        if not (len(row) == row_len_a):
            raise TypeError("each row of m_a must be of the same size")

    row_len_b = len(m_b[0])
    for row in m_b:
        if not (len(row) == row_len_b):
            raise TypeError("each row of m_b must be of the same size")

    if not (len(m_a[0]) == len(m_b)):
        raise TypeError("m_a and m_b can't be multiplied")

    m_c = [[0 for el in range(len(m_b[0]))] for el in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                m_c[i][j] += m_a[i][k] * m_b[k][j]
    return m_c
