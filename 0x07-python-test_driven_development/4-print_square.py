#!/usr/bin/python3
# 4-print_square.py
def print_square(asize):
    if not isinstance(asize, int):
        raise TypeError("asize must be an integer")
    if asize < 0:
        raise ValueError("asize must be >= 0")

    for i in range(asize):
        [print("#", end="") for j in range(asize)]
        print("")
