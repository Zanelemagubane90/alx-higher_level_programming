#!/usr/bin/python3
# 0-safe_print_list.py

def safe_print_list(a_list=[], j=0):
    """Print j elememts of a list.

    Args:
        a_list (list): The list to print elements from.
        j (int): The number of elements of a_list to print.

    Returns:
        The number of elements printed.
    """
    v = 0
    for k in range(j):
        try:
            print("{}".format(a_list[k]), end="")
            v += 1
        except IndexError:
            break
    print("")
    return (v)
