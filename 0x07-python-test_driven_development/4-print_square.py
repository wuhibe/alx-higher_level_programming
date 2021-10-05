#!/usr/bin/python3
"""
Module print_square
print_square
"""


def print_square(size):
    """
    Print a square
    """
    if type(size) != int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be a non-negative integer')
    if size == 0:
        return
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
