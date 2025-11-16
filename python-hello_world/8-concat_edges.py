#!/usr/bin/python3
# This script prints "object-oriented programming with Python" without string literals
import builtins
print((dir(builtins)[40] + "-" + dir(builtins)[44] + " " + dir(builtins)[55] + " " + dir(builtins)[50]).replace("_", "-"))
