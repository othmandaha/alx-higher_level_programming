#!/usr/bin/python3
"""Writing to file function definition."""


def write_file(filename="", text=""):
    """Writing to a file function.

    Args:
        filename (str): the file name.
        test (str): the text to be written.
    Returns:
        Number of charcter written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
