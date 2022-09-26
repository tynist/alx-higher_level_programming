#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers."""
    for item in matrix:
        lenght = len(item)
        if lenght == 0:
            print()
        for i in range(lenght):
            print("{:d}".format(item[i]), end="\n" if i == lenght - 1 else " ")
