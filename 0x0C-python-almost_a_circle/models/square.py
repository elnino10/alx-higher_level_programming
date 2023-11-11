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

    @property
    def size(self):
        """returns size of the square sides"""
        return self.width

    @size.setter
    def size(self, size):
        """sets the size of the square side

        Args:
            size (int): size
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """assigns attributes"""
        arg_list = ["id", "size", "x", "y"]
        if args is not None and len(args) > 0:
            for name, value in zip(arg_list, args):
                setattr(self, name, value)
        else:
            for name, value in kwargs.items():
                setattr(self, name, value)
