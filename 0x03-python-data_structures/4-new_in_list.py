#!/usr/bin/python
def replace_in_list(my_list, idx, element):
    new_list = my_list
    num_elements = len(new_list)
    if idx < 0 or idx => num_elements:
        return my_list
    else:
        new_list[idx] = element
    return new_list
