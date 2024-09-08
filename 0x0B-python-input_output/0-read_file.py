#!/usr/bin/python3
"""Contains a function to read file"""


def read_file(filename = ""):
    with open('filename', 'r', encoding = 'utf-8') as f:
        f.read()
