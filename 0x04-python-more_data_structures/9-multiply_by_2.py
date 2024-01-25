#!/usr/bin/python3
"""A function that returns a new dictionary with all values multiplied by 2"""


def multiply_by_2(my_dict):
    tmp_dict = my_dict.copy()
    for x in tmp_dict.keys():
        tmp_dict[x] *= 2
    return (tmp_dict)
