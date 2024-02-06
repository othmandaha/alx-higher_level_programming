#!/usr/bin/python3
"""File Reading."""


def read_file(filename=""):
    """a function for reading from a file.

    Args:
    filename (str): the file name.
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end='')
