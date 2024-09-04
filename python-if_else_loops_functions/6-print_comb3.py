#!/usr/bin/python3
for numberfirst in range(0, 9):
    for numbersecond in range(numberfirst + 1, 10):
        print(f'{numberfirst}{numbersecond}', end=', ')
