#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda j: list(map(lambda i: i**2, j)), matrix))
