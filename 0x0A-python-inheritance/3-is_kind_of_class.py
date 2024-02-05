#!/usr/bin/python3
""" is sub or or super checker """


def is_kind_of_class(obj, a_class):
    """ checks if obj is sub or super or none

    Args:
    obj (any): the object to be checkes
    a_class (any): the class to be checked
    Returns:
    if subclass or superclass - True.
    otherwise - False
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
