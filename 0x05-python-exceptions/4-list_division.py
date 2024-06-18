#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for index in range(list_length):
        try:
            elem_1 = my_list_1[i]
            elem_2 = my_list_2[i]
            result = elem_1 / elem_2
        except (TypeError, ValueError):
            result = 0
            print('wrong type')
        except ZeroDivisionError:
            result = 0
            print('division by 0')
        except IndexError:
            result = 0
            print('out of range')
            break
        finally:
            new_list.append(result)
        return new_list
