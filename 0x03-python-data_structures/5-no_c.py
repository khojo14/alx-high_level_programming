#!/usr/bin/python
def no_c(my_string):
    num_char = len(my_string)
    for i in range(num_char):
        if my_string[i] == 'c' or my_string[i] == 'C':
            del my_string[i]
    return my_string
