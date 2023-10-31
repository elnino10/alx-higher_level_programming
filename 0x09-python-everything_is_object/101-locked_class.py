#!/usr/bin/python3
"""a class that prevents the user from dynamically creating new
instance attributes, except if the new instance attribute is
called first_name
"""


class LockedClass():
    """prevents dynamic instance creation"""

    def __setattr__(self, name, value):
        """sets attribute passed by user"""
        if name == "first_name":
            super().__setattr__(name, value)
        else:
            super().__getattribute__(name)
            raise AttributeError(
                "'LockedClass' object has no attribute '{name}'")
