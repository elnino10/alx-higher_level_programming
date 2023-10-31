#!/usr/bin/python3
"""a class that prevents the user from dynamically creating new
instance attributes, except if the new instance attribute is
called first_name
"""


class LockedClass():
    """prevents dynamic instance creation"""

    def __str__(self):
        return ""

    def __setattr__(self, name, value):
        """sets attribute passed by user"""
        if name == "first_name":
            super().__setattr__(name, value)
        else:
            raise AttributeError(
                f"'{self.__class__.__name__}' object has no \
attribute '{name}'")
