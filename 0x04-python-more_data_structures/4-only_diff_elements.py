#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    singles = set()
    for elem1 in set_1:
        for elem2 in set_2:
            if elem1 != elem2:
                singles.add(elem1)
    return singles
