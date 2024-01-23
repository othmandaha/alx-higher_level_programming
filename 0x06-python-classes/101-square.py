#!/usr/bin/python3

"""The square blueprint"""


class Square:
    """The square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square.

        Args:
            size (int): the size of the square.
            position (int, int): The position of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """get the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Computes the ares of square (self)

        Returns:
            float: the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square as #."""
        if self.__size == 0:
            print("")
            return
        for i in range(0, self.position[1]):
            print("")
        for i in range(0, self.__size):
            for i in range(0, self.position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print("")

    def __str__(self):
        """Define the print() representation of a Square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
