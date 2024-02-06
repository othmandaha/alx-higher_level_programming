#!/usr/bin/python3
""" Definition of a class-to-json function."""


def class_to_json(obj):
    """a class-to-json function"""
    return obj.__dict__
