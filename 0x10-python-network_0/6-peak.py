#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    if list_of_integers == []:
        return None

    my_size = len(list_of_integers)
    if my_size == 1:
        return list_of_integers[0]
    elif my_size == 2:
        return max(list_of_integers)

    amid = int(my_size / 2)
    a_peak = list_of_integers[amid]
    if a_peak > list_of_integers[amid - 1] and a_peak > list_of_integers[amid + 1]:
        return a_peak
    elif a_peak < list_of_integers[amid - 1]:
        return find_peak(list_of_integers[:amid])
    else:
        return find_peak(list_of_integers[amid + 1:])
