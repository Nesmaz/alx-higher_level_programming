#!/usr/bin/python3
"""
A function that replaces all occurrences of an element
by another in a new list
"""


def search_replace(my_list, search, replace):
    return (list(map(lambda i: replace if i is search else i, my_list)))
