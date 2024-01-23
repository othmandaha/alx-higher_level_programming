#!/usr/bin/python3
""" A class of name square """


class Square:
    """Representation of a square"""

    def __init__(self, size=0):
        """Initialize a new square"""

        if not isinstance(size, int):
            raise TypeError("Only Numbers are accepted")
        elif size <= 0:
            raise ValueError("Inappropriate argument value")
        self.__size = size
