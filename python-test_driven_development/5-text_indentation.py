#!/usr/bin/python3
def text_indentation(text):
    """
    Return: the result of the text
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    result = ""
    for char in text:
        result += char
        if char in ".?:":
            result += "\n\n"

    lines = result.splitlines()
    for line in lines:
        print(line.strip())
