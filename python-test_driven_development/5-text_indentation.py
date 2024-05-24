#!/usr/bin/python3
"""
    Function file for text_indentation.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each characters
    `.`, `?`, `:`
    Arguments:
        text (str): Text to format.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""

    for i in range(len(text)):
        char = text[i]

        if char in ".?:":
            result += char + "\n\n"
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            i -= 1
        else:
            result += char

    result_lines = result.split("\n")
    result = "\n".join(line.strip() for line in result_lines)

    print(result)
