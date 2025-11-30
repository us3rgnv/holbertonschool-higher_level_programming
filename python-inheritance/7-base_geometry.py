# Python Inheritance - 7-base_geometry

## Description
This module defines a class `BaseGeometry` with two public instance methods:

1. `area()`: Raises an exception indicating that it is not implemented.
2. `integer_validator(name, value)`: Validates that `value` is an integer greater than 0. Raises `TypeError` or `ValueError` if the validation fails.

## Usage
```python
BaseGeometry = __import__('7-base_geometry').BaseGeometry

bg = BaseGeometry()
bg.integer_validator("my_int", 12)
bg.integer_validator("width", 89)

try:
    bg.integer_validator("name", "John")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
