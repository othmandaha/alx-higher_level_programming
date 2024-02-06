#!/usr/bin/python3
import json
"""Definition of a function for converting to JSON."""


def to_json_string(my_obj):
    """ function for converting str to JSON.

    Args:
        my_obj (any): object to be converted.
    Returns:
        the JSON representation."""
    return json.dumps(my_obj)
