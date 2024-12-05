#!/usr/bin/python3
def copy_list(a_list):
    if len(a_list) < 3:
        return a_list
    else:
        return a_list.copy()
