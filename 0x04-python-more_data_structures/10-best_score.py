#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return None

    value = 0
    key = None

    for k, v in a_dictionary.items():
        if value < v:
            value = v
            key = k

    return key
