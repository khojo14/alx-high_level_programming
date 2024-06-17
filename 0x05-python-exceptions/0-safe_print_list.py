#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nb_print = 0

    while True:
        try:
            for i in range(x):
                print(my_list[i], end="")
                nb_print += 1
            break
        except (IndexError, TypeError):
            break
    return nb_print
