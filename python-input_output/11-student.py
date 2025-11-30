#!/usr/bin/python3
""" Student module with serialization and deserialization
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
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        return self.__dict__

    def reload_from_json(self, json):
        """ Replace all attributes of the Student instance """
        for key, value in json.items():
            setattr(self, key, value)
