#!/usr/bin/python3
import sys

if __name__ == '__main__':

    argv = sys.argv
    _len = len(argv)-1
    if _len == 0:
        print('{} arguments.'.format(_len))
    elif _len == 1:
        print('{} arguments:'.format(_len))
    else:
        print(f"{_len} arguments:")

    for i in range(1, len(argv)-1):
        print(f"{i}: {argv[i]}")
