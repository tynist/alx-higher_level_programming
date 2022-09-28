#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix and
    Returns a new matrix"""
    return [list(map((lambda x: x * x), nums)) for nums in matrix]
