#!/usr/bin/python3
"""module has a class MyInt that inherits from int
"""


class MyInt(int):
    """MyInt class has == and != operators inverted

    Args:
        int (type): the parent class MyInt inherits from
    """

    def __eq__(self, value):
        """returns true if equality is true

        Args:
            value (int): value passed

        Returns:
            bool: opposite of the actual value
        """
        return super().__eq__(not value)

    def __ne__(self, value):
        """returns true if value is not equal

        Args:
            value (int): value passed

        Returns:
            bool: opposite of the actual value
        """
        return super().__ne__(not value)
