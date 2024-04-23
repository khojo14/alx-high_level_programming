#!/usr/bin/python3
def common_elements(set_1, set_2):
    common = set()
    for elem in set_1:
        for elem2 in set_2:
            if elem == elem2:
                common.add(elem)
    return common
