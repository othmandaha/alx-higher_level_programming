#!/usr/bin/pthon3
"""Defines a function for appending to a file."""


def append_write(filename="", text=""):
    """a function for appending to a file.

    Args:
        filename (str): the file name.
        text (str): the text to be appended.
    Returns:
        the number of character appended.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
