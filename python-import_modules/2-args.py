#!/usr/bin/python3
import sys

if __name__ == '__main__':
    argv = sys.argv
    _len = len(argv) - 1

    if _len == 0:
        print('{} arguments.'.format(_len))
    elif _len == 1:
        print('{} argument:'.format(_len))
    else:
        print('{} arguments:'.format(_len))

    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
