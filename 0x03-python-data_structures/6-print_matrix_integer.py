#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers."""
    for str in matrix:
        j = len(str)
        if j == 0:
            print()
        for i in range(lenght):
            print("{:d}".format(str[i]), end="\n" if i == j - 1 else " ")
