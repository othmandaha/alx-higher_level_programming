#!/usr/bin/python
"""Defines a student class."""


class student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initiation of the class.

        Args:
        first_name (str): the first name of the student.
        last_name (str): the last name of the student.
        age (int): the age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary represention of Student."""
        return self.__dict__
