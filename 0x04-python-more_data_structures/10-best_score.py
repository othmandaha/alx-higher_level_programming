#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        best_score = 0
        name = None
        for key, value in a_dictionary.items():
            if value > best_score:
                best_score = value
                name = key
        return name
