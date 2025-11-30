#!/usr/bin/python3
"""
Module: 11-square
Defines a Square class that inherits from Rectangle.
Size is private, validated as a positive integer, and area() is implemented.
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
        super().__init__(size, size)

    def __str__(self):
        """
        Return the string representation of the Square.

        Format: [Square] width/height
        """
        return "[Square] {}/{}".format(self._Rectangle__width,
                                       self._Rectangle__height)
