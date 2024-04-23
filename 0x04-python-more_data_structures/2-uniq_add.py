#!/usr/bin/python3
def uniq_add(my_list=[]):
    single = set()
    sum_ints = 0
    for num in my_list:
        if num not in single:
            sum_ints += num
            single.add(num)
    return sum_ints
