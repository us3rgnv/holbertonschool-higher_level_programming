#!/usr/bin/python3
def no_c(my_string):
    """Return a string without characters 'c' and 'C'."""
    new_str = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_str += char
    return new_str
