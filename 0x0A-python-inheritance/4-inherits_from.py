#!/usr/bin/python3

"""
 module for inherits_from.
"""


def inherits_from(obj, a_class):
    """Return if the object is an instance that inherited from the specified"""
    return isinstance(obj, a_class) and type(obj) != a_class
