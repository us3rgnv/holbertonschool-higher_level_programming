#!/usr/bin/python3
"""
Module that defines a function to check if an object is an instance of
a specified class or of a class that inherited from it.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or a subclass, else False.
    """
    return isinstance(obj, a_class)
