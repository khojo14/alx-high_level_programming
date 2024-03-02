#!/usr/bin/python3
def uppercase(str):
    conv_str = ""
    for c in str:
        val = ord(c)
        if 97 <= val <= 122:
            conv_str += chr(val - 32)
        else:
            conv_str += c
    print("{}".format(conv_str))
