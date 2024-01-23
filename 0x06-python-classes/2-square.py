#!/usr/bin/python3

"""a square class"""


class Square:
    """ a square blueprint """

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
        size (int): the size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
