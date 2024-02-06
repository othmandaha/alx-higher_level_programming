#!/usr/bin/python3
"""Define loading from json file function."""
import json


def load_from_json_file(filename):
    """Creates an object from JSON file."""
    with open(filename) as file:
        json.load(filename)
