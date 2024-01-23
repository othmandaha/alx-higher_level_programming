#!/usr/bin/python3

"""The square blueprint"""


class Square:
    """The square class"""

    def __init__(self, size=0):
        """Initialize the square.

        Args:
            size (int): the size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Computes the ares of square (self)

        Returns:
            float: the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square as #."""
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
