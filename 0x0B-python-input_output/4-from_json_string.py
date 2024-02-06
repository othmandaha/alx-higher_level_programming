#!/usr/bin/python3
"""Definition of a JSON-Object converter function."""
import json


def from_json_string(my_str):
    """The Json-Object converting function."""
    return json.loads(my_str)
