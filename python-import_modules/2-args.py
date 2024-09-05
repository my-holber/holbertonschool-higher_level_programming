#!/usr/bin/env python3
import sys

if __name__ == '__main__':

    argv = sys.argv
    _len = len(argv)-1
    if _len == 0:
        print(f"{_len} arguments.")
    elif _len == 1:
        print(f"{_len} arguments:")
    else:
        print(f"{_len} arguments:")

    for i in range(1, len(argv)-1):
        print(i, argv[i])
