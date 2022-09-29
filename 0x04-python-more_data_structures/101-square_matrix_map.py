#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    """Computes the square value of all integers of a matrix using map"""
    return list(map(lambda rows: list(map(lambda cols: cols**2, rows)), matrix))
