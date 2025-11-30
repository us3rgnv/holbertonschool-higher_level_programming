#!/usr/bin/python3
"""
Module that defines a class BaseGeometry with a public method area().
"""


class BaseGeometry:
    """BaseGeometry class with area() method that is not implemented."""

    def area(self):
        """Raises an Exception indicating area() is not implemented."""
        raise Exception("area() is not implemented")
