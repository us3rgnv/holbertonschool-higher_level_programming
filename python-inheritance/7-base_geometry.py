#!/usr/bin/python3
"""
Module: 7-base_geometry
Defines a class BaseGeometry with two public instance methods:
1. area(): raises an exception
2. integer_validator(name, value): validates that value is an integer > 0
"""

class BaseGeometry:
    """Class BaseGeometry with area and integer validation."""

    def area(self):
        """Raises an Exception indicating area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates 'value' as an integer greater than 0.

        Args:
            name (str): The name of the value
            value (int): The value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value <= 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
