#!/usr/bin/python3
""" a base geometry BluePrint """


class BaseGeometry:
    """ the Base geometry class """

    def area(self):
        """ are calculator """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validate value as integer
        Args:
            name (str): value name
            value (int): the value
        Raises:
            TypeError: if value is not an int
            ValueError: if value is equal or less than 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
