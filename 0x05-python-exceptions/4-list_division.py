#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for index in range(list_length - 1):
        try:
            new_list.append(my_list_1[index]/my_list_2[index])
        except TypeError:
            new_list.append(0)
            print('wrong type')
            pass
        except ZeroDivisionError:
            new_list.append(0)
            print('division by 0')
            pass
        except IndexError:
            new_list.append(0)
            print('out of range')
            break
        finally:
            return new_list
