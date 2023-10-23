#!/usr/bin/python3
# 2-safe_print_list_integers.py

def safe_print_list_integers(xlist=[], indx=0):
    j = 0
    for y in range(0, indx):
        try:
            print("{:d}".format(xlist[y]), end="")
            j += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (j)
