#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    
    # Insert two new lines after each of these characters: '.', '?', ':'
    result = ""
    for char in text:
        result += char
        if char in ".?:":
            result += "\n\n"
    
    # Print each line, stripping any leading or trailing whitespace
    lines = result.splitlines()
    for line in lines:
        print(line.strip())
