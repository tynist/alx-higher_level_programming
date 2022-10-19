#!/usr/bin/python3
"""Matrix division"""


def matrix_divided(matrix, div):
    """
    Args: Divides all element of a matrix.
        :param matrix: must be a list of lists of integers or floats.
        :param div: a number (integer or float), can't be equal to 0,
                    used in dividing all elements of the matrix,
                    rounded to 2 decimal places.
    Raises:
    TypeError - if list of lists is not integers or floats, if each row of the matrix is not same size.
    ZeroDivisionError - if div equal to 0.

    Returns: new matrix.
    """
    import decimal
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(error_msg)
    len_rows = []
    row_count = 0
    for row in matrix:
        if type(row) is not list:
            raise TypeError(error_msg)
        len_rows.append(len(row))
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError(error_msg)
        row_count += 1
    if len(set(len_rows)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if int(div) == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = list(map(lambda row:
                          list(map(lambda x: round(x/div, 2), row)), matrix))
    return new_matrix
