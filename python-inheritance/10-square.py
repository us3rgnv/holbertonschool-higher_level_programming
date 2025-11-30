#!/usr/bin/python3
"""
Module: 10-square
Defines a Square class that inherits from Rectangle.
Size is private and validated as a positive integer.
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Square class inheriting from Rectangle."""

    def __init__(self, size):
        """
        Initialize a Square.

        Args:
            size (int): Size of the square sides (must be positive integer)
        """
        self.integer_validator("size", size)
        self.__size = size
        # Call Rectangle initializer with width and height equal to size
        super().__init__(size, size)
