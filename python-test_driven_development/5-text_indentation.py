#!/usr/bin/python3
"""
 This function that prints a text with 2 new lines
 after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Return: the result of the text
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    skip_next = False
    for idx, i in enumerate(text):
        if skip_next and i == ' ':
            skip_next = False
            continue
        elif skip_next:
            skip_next = False  # Do not skip valid characters like letters
        if i in [".", ":", "?", "!"]:
            print(i, end="\n")
            print()
            skip_next = True
        else:
            print(i, end="")
#!/usr/bin/python3
"""
    Function file for text_indentation.
"""


def text_indentation(text):
    """
        Prints a text with 2 new lines after each characters
        `.`, `?`, `:`
        Arguments:
            text (str): Text to formated.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    s = text[:]

    for d in ".?:":
        list_text = s.split(d)
        s = ""
        for i in list_text:
            i = i.strip(" ")
            s = i + d if s is "" else s + "\n\n" + i + d

    print(s[:-3], end="")
