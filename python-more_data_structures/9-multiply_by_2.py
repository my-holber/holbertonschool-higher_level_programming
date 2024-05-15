#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    _dict = {}
    for k, v in sorted(a_dictionary.items()):
        _dict[k] = v * 2
    return (_dict)
