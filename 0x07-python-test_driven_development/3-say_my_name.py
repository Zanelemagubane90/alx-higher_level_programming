#!/usr/bin/python3
# 3-say_my_name.py
def say_my_name(f_name, l_name=""):
    if not isinstance(f_name, str):
        raise TypeError("f_name must be a string")
    if not isinstance(l_name, str):
        raise TypeError("l_name must be a string")
    print("My name is {} {}".format(f_name, l_name))
