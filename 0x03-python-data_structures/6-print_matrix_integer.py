#!/usr/bin/python3
def print_matrix_integer(matrix = [[]]):
    if len(matrix) == 1:
        print("")
        return
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i]) - 1):
            print(matrix[i][j], end=" ")
        print(matrix[i][len(matrix[i])-1], end="")
        print("")
