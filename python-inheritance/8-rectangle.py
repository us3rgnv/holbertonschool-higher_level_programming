#!/usr/bin/python3
"""
Module: 8-rectangle
Defines a Rectangle class that inherits from BaseGeometry.
Width and height are private and validated by BaseGeometry's integer_validator.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """
        Initialize a Rectangle.

        Args:
            width (int): Width of the rectangle (must be positive integer)
            height (int): Height of the rectangle (must be positive integer)
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
