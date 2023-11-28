#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number == abs(number)
newNumber = number % 10
if number < 6 and number != 0:
    print(f"Last digit of {number} is {newNumber} and is less 6 and not 0")
if number > 5:
    print(f"Last digit of {number} is {newNumber} and is greater than 5")
elif number == 0:
    print(f"Last digit of {number} is {newNumber} and is 0")
