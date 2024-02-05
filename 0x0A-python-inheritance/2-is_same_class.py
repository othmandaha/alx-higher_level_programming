#!/usr/bin/python3
""" checking a class """


def is_same_class(obj, a_class):
    """ Checks if an object is an instance of a class

    Args:
    obj (any): the objec to be checked
    a_class (any): the class to be checked
    Returns: If object an instance of class - True.
    otherwise - False
    """
    if type(obj) == a_class:
        return True
    return False
