#!/usr/bin/python3
# 101-safe_function.py
import sys

def safe_function(xct, *argsz):
    try:
        out_put = xct(*argsz)
        return (out_put)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
