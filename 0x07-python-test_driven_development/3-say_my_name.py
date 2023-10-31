#!/usr/bin/python3
"""the say_my_name function prints the argument(s) passed to it as names
>>> say_my_name("Foo", "Bar")
My name is Foo Bar
"""


def say_my_name(first_name, last_name=""):
    """Returns first name and last name if they are passed as arguments and
    are atrings else it raises exceptions as required

    parameters: first_name, last_name=""

    exceptions: first_name must be a string
                last_name must be a string

    returns: My name is <first name> <last name>
    """
    if first_name or first_name == "":
        if not isinstance(first_name, str):
            raise TypeError('first_name must be a string')
        if not isinstance(last_name, str):
            raise TypeError('last_name must be a string')

        print(f"My name is {first_name} {last_name}")
    else:
        raise TypeError('first_name must be a string')
