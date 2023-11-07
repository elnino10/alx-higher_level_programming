#!/usr/bin/python3
"""
0-read_file module has a function that reads a text file
(UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """reads a text file and print to stdout

    Args:
        filename (str, optional): name of file to read from. Defaults to "".
    """
    with open(filename, "r", encoding="utf-8") as my_file:
        print(my_file.read())
