#!/usr/bin/python3
""" function for checking object """


def inherits_from(obj, a_class):
    """checks if obj is inherited

    Args:
    obj (any): the object to be checked
    a_class (any): the class
    Returns:
    if obj is subclass - True.
    Otherwise - False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
