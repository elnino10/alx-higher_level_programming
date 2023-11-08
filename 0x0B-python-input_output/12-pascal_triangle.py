#!/usr/bin/python3
"""function def pascal_triangle(n): that returns a list of lists
of integers representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the pascal's triangle

    Args:
        n (int): number of lists

    Return:
        an empty list if n <= 0, or a list of lists of integers otherwise
    """
    p_tri = [[]]
    row = 1
    while row <= n:
        triangle_row = []
        for col in range(row):
            # get value for current cell
            if col in (0, row - 1):
                # if first or last cell in current row
                cell_val = 1
            else:
                # add the two cells above
                cell_val = p_tri[row - 1][col - 1] + p_tri[row - 1][col]
            triangle_row.append(cell_val)
        p_tri.append(triangle_row)
        row += 1
    # slice out the initializing empty list before returning
    return p_tri[1:]
