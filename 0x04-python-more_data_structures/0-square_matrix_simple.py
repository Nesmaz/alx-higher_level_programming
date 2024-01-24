#!/usr/bin/python3
"""A function that computes the square value of all integers of a matrix"""


def square_matrix_simple(matrix=[]):
    tmp = []
    for i in matrix:
        tmp.append(list(map(lambda i: i**2, i)))
    return (tmp)
