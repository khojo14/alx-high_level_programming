#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nb_print = 0

    while True:
        try:
            for i in range(x):
                print("{:d}".format(my_list[i]), end="")
                nb_print += 1
            break
        except(TypeError, ValueError):
            pass
        except IndexError:
            break
    print()
    return nb_print