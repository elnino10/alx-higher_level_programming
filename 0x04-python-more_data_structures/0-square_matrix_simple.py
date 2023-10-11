#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    mat_row = []
    for row in matrix:
        mat_el = []
        for num in row:
            mat_el.append(num ** 2)
        mat_row.append(mat_el)
    return mat_row
