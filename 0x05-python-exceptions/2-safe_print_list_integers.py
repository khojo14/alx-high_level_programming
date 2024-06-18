#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nb_print = 0
    i = 0

    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            nb_print += 1
            break
        except(TypeError, ValueError):
            pass
        i += 1
    print()
    return nb_print
