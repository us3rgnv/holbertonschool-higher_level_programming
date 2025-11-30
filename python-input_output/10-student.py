#!/usr/bin/python3
""" Student module
"""

class Student:
    """ Student class
    """

    def __init__(self, first_name, last_name, age):
        """ Initialize a Student instance """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieve a dictionary representation of the Student.
            If attrs is a list of strings, only include those attributes.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            # Filter attributes to only those in attrs
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        return self.__dict__
