#!/usr/bin/python3
""" an addition function"""


def add_integer(a, b=98):
    """Return the addition result of a and b
    Raises:
        TypeError: if a or b is not int or float
    """
    if not isinstance(a, int) or not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) or not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
