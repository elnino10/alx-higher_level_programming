#!/usr/bin/python3
"""a class that prevents the user from dynamically creating new
instance attributes, except if the new instance attribute is
called first_name
"""


class LockedClass():
    """prevents dynamic instance creation"""

    __slots__ = ["first_name"]
