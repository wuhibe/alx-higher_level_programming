#!/usr/bin/python3
'''
Module for pascal_triangle.
'''


def pascal_triangle(n):
    """ Pascal Triangle """

    triangle = []
    if n <= 0:
        return triangle

    triangle = [[1]]
    for i in range(n - 1):
        line = triangle[-1]
        aux = [1]
        for i in range(len(line) - 1):
            aux.append(line[i] + line[i + 1])
        aux.append(1)
        triangle.append(aux)
    return triangle
