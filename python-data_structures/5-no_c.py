#!/usr/bin/python3
def no_c(my_string):
    result_string = ""
    index = ["c", "C"]
    for i in my_string:
        if i not in index:
            result_string += i
    return (result_string)
