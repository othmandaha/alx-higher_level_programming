#!/usr/bin/python3
"""A square blueprint."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represents a Square."""

    def __init__(self, size):
        """Square initialized.

        Args:
            size (int): the size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
