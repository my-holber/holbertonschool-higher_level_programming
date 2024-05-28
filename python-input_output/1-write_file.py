#!/usr/bin/python3
""" Module that contains a function that reads from a file """


def write_file(filename="", text=""):
    """
    Reads a text file (UTF8) and prints it to stdout.
    """

    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
