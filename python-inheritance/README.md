# 0-lookup

## Description
This module defines a function `lookup` that returns a list of available attributes and methods of an object. It can be used to inspect built-in types, user-defined classes, or any Python object.

## File
`0-lookup.py`

## Function

### `lookup(obj)`
- **Prototype:** `def lookup(obj):`
- **Arguments:** `obj` - any Python object
- **Returns:** A list of strings representing the attributes and methods of the object.
- **Example:**

```python
#!/usr/bin/python3
lookup = __import__('0-lookup').lookup

class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))
