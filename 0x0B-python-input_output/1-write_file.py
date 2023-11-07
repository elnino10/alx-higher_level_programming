#!/usr/bin/python3
"""
module contains write_file(), a function that writes a string
to a text file (UTF8) and returns the number of characters written
"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)

    Args:
        filename (str): file name. Defaults to "".
        text (str): string or text to be written to file.
        Defaults to "".

    Return:
        number of characters written
    """
    with open(filename, "w", encoding="utf-8") as my_file:
        n_chars = my_file.write(text)
        return n_chars
