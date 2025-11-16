#!/usr/bin/python3
# This script assigns a random signed number to `number` and prints whether it is positive, zero, or negative

import random

# Generate a random number between -10 and 10
number = random.randint(-10, 10)

# Check if the number is positive, zero, or negative
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
