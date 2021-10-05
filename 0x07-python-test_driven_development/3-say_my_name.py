#!/usr/bin/python3
"""
Module say_my_name
say_my_name
"""


def say_my_name(first_name, last_name=""):
    """
    Print Full Nname for a person.
    """
    if type(first_name) != str:
        raise TypeError('First_name must be a string')
    if type(last_name) != str:
        raise TypeError('Last_name must be a string')
    print("My name is " + first_name + " " + last_name)
