#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
if number >= 0:
    last_digit = number % 10
else:
    last_digit = number % -10
abc = 'Last digit of'
if number % 10 > 5:
    print(f"{abc} {number} is {last_digit} and is greater than 5")
elif number % 10 == 0:
    print(f"{abc} {number} is {last_digit} and is 0")
else:
    print(f"{abc} {number} is {last_digit} and is less than 6 and not 0")
