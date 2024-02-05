#!/usr/bin/python3
""" a rectangle blueprint """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """the Rectangle class"""

    def __init__(self, width, height):
        """initialise a new rectangle.

        Args:
            width (int): the width of the rectangle.
            height (int): the height fo the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """for print() and str()"""
        string = '[' + str(self.__class__.__name__) + '] '
        string += str(self.__width) + '/' + str(self.__height)
        return string
