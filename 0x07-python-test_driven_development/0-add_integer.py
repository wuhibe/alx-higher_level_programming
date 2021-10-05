#!/usr/bin/python3
"""
Module add-integer
add two integers
"""


def add_integer(a, b=98):
    """ This function return the sum of intgers
    or the int cast of floats
    """

    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)

    return a + b
