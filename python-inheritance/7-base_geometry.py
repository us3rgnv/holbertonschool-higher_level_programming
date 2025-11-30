#!/usr/bin/python3
"""
Module: BaseGeometry
Contains the BaseGeometry class with area and integer_validator methods.
"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Public method: raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is an integer > 0"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
