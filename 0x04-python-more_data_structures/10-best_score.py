#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        best_score = 0
        name = None
        for keys, values in a_dictionary.items():
            if value > best_score:
                name = keys
        return name
