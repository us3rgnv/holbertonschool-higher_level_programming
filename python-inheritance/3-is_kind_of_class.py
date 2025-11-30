# Python Inheritance - 3-is_kind_of_class

## Description
This module defines a function `is_kind_of_class` that checks whether an object
is an instance of a specified class or of a class that inherited from it.

## Usage
```python
is_kind_of_class = __import__('3-is_kind_of_class').is_kind_of_class

a = 1
print(is_kind_of_class(a, int))    # True
print(is_kind_of_class(a, float))  # False
print(is_kind_of_class(a, object)) # True
