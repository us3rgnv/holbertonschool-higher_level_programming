#!/usr/bin/python3
"""
This module defines a Rectangle class with width and height attributes,
methods to calculate area and perimeter, print the rectangle using the symbol
stored in print_symbol, repr() for eval(), deletion message, and a class
attribute number_of_instances to track active Rectangle instances.
"""

class Rectangle:
    """Rectangle class with width, height, area, perimeter, string representation,
    eval()-friendly repr(), deletion message, instance counting, and customizable print symbol.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance with optional width and height.
        Increment the class attribute number_of_instances.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        """Return the rectangle as a string made of print_symbol characters.
        If width or height is 0, return an empty string.
        """
        if self.width == 0 or self.height == 0:
            return ""
        symbol = str(self.print_symbol)
        return '\n'.join([symbol * self.width for _ in range(self.height)])

    def __repr__(self):
        """Return a string representation of the rectangle
        to recreate a new instance using eval().
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print a message when a Rectangle instance is deleted
        and decrement the number_of_instances class attribute.
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
