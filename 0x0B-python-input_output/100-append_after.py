#!/usr/bin/python3
"""function that inserts a line of text to a file, after
each line containing a specific string (see example)
"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file

    Args:
        filename (str, optional): string to search for. Defaults to "".
        search_string (str, optional): _description_. Defaults to "".
        new_string (str, optional): new string to append. Defaults to "".
    """
    with open(filename, "r+", encoding="utf-8") as my_file:
        read_ln = my_file.readlines()
        new_file = []
        for line in read_ln:
            new_file.append(line)
            if search_string in line:
                new_file.append(new_string)

    with open(filename, "w", encoding="utf-8") as my_file:
        for line in new_file:
            my_file.write(line)
