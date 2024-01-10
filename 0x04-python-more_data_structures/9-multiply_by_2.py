#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    keys = a_dictionary.keys()
    new = {}
    for key in keys:
        new[key] = a_dictionary[key] * 2
    return new
