#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for el in row:
            if row.index(el) != (len(row) - 1):
                print("{:d}".format(el), end=" ")
            else:
                print("{:d}".format(el), end="")
        print()
