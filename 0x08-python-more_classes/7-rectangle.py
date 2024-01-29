#!/usr/bin/python3
"""a class"""


class Rectangle:
    """a Rectangle class"""

    """Attributes:
        number_of_instances (int): counter of instances
        print_symbole (any): the symbole to be printed as rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialize an object

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangele
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets the height of the ractangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates the area of a rectangle"""
        return self.height * self.width

    def perimeter(self):
        """calculates the perimeter of a rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ("")

        rec = []
        for i in range(self.height):
            [rec.append(str(self.print_symbol)) for j in range(self.width)]
            if i != self.__height - 1:
                rec.append("\n")
        return ("".join(rec))

    def __repr__(self):
        rec = "Rectangle(" + str(self.__width)
        rec += ", " + str(self.__height) + ")"
        return (rec)

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
