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

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the js representation of a list to a file.
        Args:
            list_objs (list): the list to be written.
        """
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dict = [obj.to_dicionary() for obj in list_objs]
                f.write(Base.to_json_string(list_dict))
