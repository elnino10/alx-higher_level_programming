#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as err:
        print("Exception: ", end="", file=stderr)
        for arg in err.args:
            print(arg, file=stderr)
        return False
