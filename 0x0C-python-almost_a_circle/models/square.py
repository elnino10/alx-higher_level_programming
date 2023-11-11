#!/usr/bin/python3
"""module square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """the class Square that inherits from Rectangle

    Args:
        Rectangle (obj): base class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """constructor

        Args:
            size (int): width
            x (int, optional): Defaults to 0.
            y (int, optional): Defaults to 0.
            id (int, optional): instance identification. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.width
        )
