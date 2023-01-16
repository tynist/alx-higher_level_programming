#!/usr/bin/python3
"""Find a peak model"""


def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers"""
    if list_of_int == []:
        return None

    length = len(list_of_int)
    if length == 1:
        return list_of_int[0]
    elif length == 2:
        return max(list_of_int)

    mid = int(length / 2)
    peak = list_of_int[mid]
    if peak > list_of_int[mid - 1] and peak > list_of_int[mid + 1]:
        return peak
    elif peak < list_of_int[mid - 1]:
        return find_peak(list_of_int[:mid])
    else:
        return find_peak(list_of_int[mid + 1:])
