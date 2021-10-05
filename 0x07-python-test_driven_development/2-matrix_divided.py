#!/usr/bin/python3
"""
Module Matrix_divided
Divided matrix
"""


def matrix_divided(matrix, div):
    """Returns a matrix
    of results of a divided matrix
    """
    if type(matrix) != list or len(matrix) == 0 or matrix[0] is None:
        raise TypeError("Matrix must be a matrix (list of lists) of \
integers/floats")

    for r in matrix:
        if len(r) == 0:
            raise TypeError("Matrix must be a matrix (list of lists) of \
integers/floats")
        for i in r:
            if type(i) != int and type(i) != float:
                raise TypeError("Matrix must be a matrix (list of lists) of \
integers/floats")

    lr = []
    for r in matrix:
        lr.append(len(r))
    if not all(item == lr[0] for item in lr):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    nm = [[round(x / div, 2) for x in r] for r in matrix]

    return nm
