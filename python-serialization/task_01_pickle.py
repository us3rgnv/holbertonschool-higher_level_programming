#!/usr/bin/python3
"""
Module for serializing and deserializing a custom Python object using pickle.
"""

import pickle


class CustomObject:
    """
    Custom object class with name, age, and is_student attributes.
    Provides methods to display, serialize, and deserialize instances.
    """

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the attributes of the object in the specified format.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance to a file using pickle.
        Returns None if any exception occurs.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an instance from a file using pickle.
        Returns None if file does not exist or is malformed.
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
            if isinstance(obj, cls):
                return obj
            return None
        except Exception:
            return None
