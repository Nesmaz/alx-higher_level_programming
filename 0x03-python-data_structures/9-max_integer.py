#!/usr/bin/python3
"""A function that finds the biggest integer of a list"""


def max_integer(my_list=[]):
    if not my_list:
        return None
    biggest = 0
    for elem in my_list:
        if elem > biggest:
            biggest = elem
    return biggest
