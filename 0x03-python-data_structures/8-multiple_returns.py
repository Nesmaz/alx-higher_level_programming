#!/usr/bin/python3
"""
A function that returns a tuple with the length of a string
and its first character
"""


def multiple_returns(sentence):
    return (len(sentence), sentence[0] if sentence != "" else None)
