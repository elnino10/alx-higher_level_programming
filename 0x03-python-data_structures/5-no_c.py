#!/usr/bin/python3

def no_c(my_string):
    new_string = ""

    for el in my_string:
        if el == 'c' or el == 'C':
            continue
        new_string += el

    return new_string
