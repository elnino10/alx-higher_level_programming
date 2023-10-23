#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        res = fct(*args)
        return res
    except ZeroDivisionError as err:
        print("Exception: ", end="", file=stderr)
        for el in err.args:
            print(el, file=stderr)
    except IndexError as err:
        print("Exception: ", end="", file=stderr)
        for el in err.args:
            print(el, file=stderr)
