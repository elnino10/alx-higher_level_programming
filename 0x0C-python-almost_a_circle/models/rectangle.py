#!/usr/bin/python3
"""rectangle module
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle inherits from Base

    Args:
        Base (obj): base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiates the class

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int, optional): Defaults to 0.
            y (int, optional): Defaults to 0.
            id (int, optional): identification. Defaults to None.
        """
        super().__init__(id)
        for k, v in zip((width, height, x, y), ("width", "height", "x", "y")):
            if not isinstance(k, int) or k is None:
                raise TypeError(f"{v} must be an integer")

        for arg, name in zip((width, height), ("width", "height")):
            if arg <= 0:
                raise ValueError(f"{name} must be > 0")

        for arg, name in zip((x, y), ("x", "y")):
            if arg < 0:
                raise ValueError(f"{name} must be >= 0")
        self.__width, self.__height = width, height
        self.__x, self.__y = x, y

    @property
    def width(self):
        """gets the width"""
        return self.__width

    @width.setter
    def width(self, width):
        """sets the width

        Args:
            value (int): width
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """gets the height"""
        return self.__height

    @height.setter
    def height(self, height):
        """sets the height

        Args:
            height (int): height
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """gets the value of x"""
        return self.__x

    @x.setter
    def x(self, x):
        """sets the value of x

        Args:
            x (int): x
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """gets the value y"""
        return self.__y

    @y.setter
    def y(self, y):
        """sets the value of y

        Args:
            y (int): y
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """returns the area value of the Rectangle instance"""
        return self.__height * self.__width

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        print(
            "{}".format("\n" * self.__y + " " * self.__x)
            + "".join(
                "#" * self.__width
                + ("\n" + " " * self.__x + ("#" * self.__width)) * (
                    self.__height - 1)
            )
        )

    def __str__(self):
        """return string to stdout"""
        return "".join(
            "[{}] ({}) {}/{} - {}/{}".format(
                self.__class__.__name__,
                self.id,
                self.__x,
                self.__y,
                self.__width,
                self.__height,
            )
        )

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        arg_list = ["id", "width", "height", "x", "y"]
        if args is not None and len(args) > 0:
            for name, arg in zip(arg_list, args):
                setattr(self, name, arg)
        else:
            for key, value in kwargs.items():
                if key in arg_list:
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
