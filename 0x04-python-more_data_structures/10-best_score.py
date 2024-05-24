#!/usr/bin/python3
def best_score(a_dictionary):
    if  a_dictionary == None:
        return None
    else:
        new_dict = {}
        value = 0
        name_key = ""
        for k, v in a_dictionary.items():
            if value < v:
                new_dict.clear()
                new_dict[k] = v
                value = v
                name_key = k
        return name_key
