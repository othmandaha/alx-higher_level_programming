#!/usr/bin/python3
"""Defines a Json-file writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Json-File function."""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
