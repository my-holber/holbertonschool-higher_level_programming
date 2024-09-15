#!/usr/bin/python3
def text_indentation(text):
    """
    Return: the result of the text
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    result = text.replace('.', '.\n\n').replace
    ('?', '?\n\n').replace(':', ':\n\n')
    lines = result.split('\n')
    cleaned_lines = [line.strip() for line in lines]
    print('\n'.join(cleaned_lines))
