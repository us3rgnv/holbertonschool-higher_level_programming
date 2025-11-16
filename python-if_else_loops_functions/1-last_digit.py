#!/usr/bin/python3
# This script prints the last digit of a random number and a message

import random

number = random.randint(-10000, 10000)
last_digit = number % 10 if number >= 0 else -(-number % 10)

print("Last digit of", number, "is", last_digit, end="")

if last_digit > 5:
    print(" and is greater than 5")
elif last_digit == 0:
    print(" and is 0")
else:
    print(" and is less than 6 and not 0")
