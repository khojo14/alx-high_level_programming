#!/usr/bin/python3
def print_list_integer(my_list=[]):
    num_elements = len(my_list)
    for i in range(num_elements):
        print('{:d}'.format(my_list[i]))
