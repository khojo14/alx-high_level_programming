#!/usr/bin/python
def print_reversed_list_integer(my_list=[]):
    num_elements = -len(my_list) -1
    for i in range(-1, num_elements, -1):
        print('{}'.format(my_list[i]))
