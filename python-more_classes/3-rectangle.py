#!/usr/bin/python3
"""
This module defines a Rectangle class with width and height attributes,
including methods to calculate area, perimeter, and to print the rectangle
using the '#' character.
"""

class Rectangle:
    """Rectangle class with width, height, area, perimeter, and string representation."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance with optional width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle.
        If width or height is 0, perimeter is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return the rectangle as a string made of '#' characters.
        If width or height is 0, return an empty string.
        """
        if self.width == 0 or self.height == 0:
            return ""
        lines = ['#' * self.width for _ in range(self.height)]
        return '\n'.join(lines)

    def __repr__(self):
        """Return the official string representation of the rectangle object."""
        return f"<{self.__class__.__name__} object at {hex(id(self))}>"
