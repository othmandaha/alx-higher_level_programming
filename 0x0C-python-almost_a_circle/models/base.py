#!/usr/bin/python3
"""base class definition"""
import json


class Base:
    """Base class.

    this class will be the base of all other classes in this project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """New base initiation.

        Args:
            id (int): new base identity.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return json formated string."""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
