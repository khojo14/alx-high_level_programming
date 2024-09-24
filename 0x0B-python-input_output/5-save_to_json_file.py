#!usr/bin/python3
"""contains a function and the json module"""


import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON representation"""
    with open(filename,'w',encodigng="utf-8") as file:
        file.write(json.dumps(my_obj)
