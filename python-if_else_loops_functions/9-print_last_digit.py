#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = abs(number)
    _result = number % 10
    print("{:d}".format(_result), end=(""))
    return(_result)
