#!/usr/binpython3
def search_replace(my_list, search, replace):
    copy_list = my_list.copy()
    new_list = []
    for num in copy_list:
        if num == search:
            num = replace
        new_list.append(num)
    return new_list
