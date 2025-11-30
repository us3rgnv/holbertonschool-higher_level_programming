#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list
and provides a method to print the list in sorted order.
"""


class MyList(list):
    """Custom list class that can print itself sorted."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))

