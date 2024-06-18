#!/usr/bin/python3
def safe_print_division(a, b):
    while True:
        try:
            result = a/b
        except ZeroDivisionError:
            result = None
            break
        finally:
            print("Inside result: {}".format(result))
    return result
