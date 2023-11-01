#!/usr/bin/python3
"""Module has a function text_indentation that  prints a text with
2 new lines after each of these characters: ., ? and :


"""


def text_indentation(text):
    """prints text with 2 new lines when specific characters encountered
    Those specific characters are in a list (symbols)
    flag is set when a symbol is encountered and unset when the next
    character after the symbol (which is a whitespace) is removed
    """
    if text:
        if not (isinstance(text, str)):
            TypeError("text must be a string")

        if isinstance(text, int) or isinstance(text, float):
            raise TypeError("text must be a string")

        symbols = ('.', '?', ':')
        flag = False

        for char in text:
            if flag and char == " ":
                flag = False
            elif flag and not (char == " "):
                print(char, end="")
                flag = False
            else:
                print(char, end="")
            if char in symbols:
                flag = True
                print("\n")
    else:
        raise TypeError("text must be a string")
