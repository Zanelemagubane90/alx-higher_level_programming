#!/usr/bin/python3
# 3-safe_print_division.py

def safe_print_division(x, y):
    try:
        a = x / y
    except (TypeError, ZeroDivisionError):
        a = None
    finally:
        print("Inside result: {}".format(a))
    return (a)
