#!/usr/bin/python3
"""This class is the "base" of all other classes in this project
"""


class Base:
    """base class of the classes for this project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """manages id attribute in all future classes and to avoid
        duplicating the same code

        Args:
            id (int, optional): identification. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
