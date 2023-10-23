#!/usr/bin/python3
# 1-safe_print_integer.py
def safe_print_integer(avl):
    try:
        print("{:d}".format(avl))
        return (True)
    except (TypeError, ValueError):
        return (False)
