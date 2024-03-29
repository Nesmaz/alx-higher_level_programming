#!/usr/bin/python3
"""A function that converts a Roman numeral to an integer"""


def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    for char in reversed(roman_string):
        value = roman_numerals[char]

        if value >= prev_value:
            total += value
        else:
            total -= value

        prev_value = value

    return total

