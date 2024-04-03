#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    num_elements = len(my_list)
    if idx < 0 or idx => num_elements:
        return my_list
    else:
        my_list[idx] = element
    return my_list
