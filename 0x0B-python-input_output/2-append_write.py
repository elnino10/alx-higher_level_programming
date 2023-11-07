#!/usr/bin/python3
"""
module contains append_write() function that appends a string
at the end of a text file (UTF8) and returns the number of characters added
"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)

    Args:
        filename (str): file name. Defaults to "".
        text (str): string of text. Defaults to "".
    Return:
        number of characters added
    """
    with open(filename, "a", encoding="utf-8") as my_file:
        n_chars = my_file.write(text)
        return n_chars
