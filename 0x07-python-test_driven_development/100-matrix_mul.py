#!/usr/bin/python3
"""Multiplies two matrix"""


def matrix_mul(m_a, m_b):
    """
     Args: Multiplies two matrices by using the module NumPy
         :param m_a: list of lists of integers or floats,
         :param m_b: list of lists of integers or floats.

    Raises:
        TypeError - if m_a and m_b is not a list, list of lists,
        one element of those list of lists is not an integer or a float,
        is not a rectangle (all ‘rows’ should be of the same size).

    ValueError - if m_a, m_b is empty (it means: = [] or = [[]])
    or can’t be multiplied.
     """
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")

    # variables to verify if both m_a and m_b can be multiplied
    num_colum1 = 0
    num_row2 = 0

    # Check requirements for matrix m_a
    if m_a == []:
        raise ValueError("m_a can't be empty")
    for row1 in m_a:
        if type(row1) != list:
            raise TypeError("m_a must be a list of lists")
        len1 = len(m_a[0])
        if row1 == []:
            raise ValueError("m_a can't be empty")
        if len1 != len(row1):
            raise TypeError("each row of m_a must be of the same size")
        num_colum1 = len(row1)
        for column1 in row1:
            if type(column1) != int and type(column1) != float:
                raise TypeError("m_a should contain only integers or floats")

    # Check requirements for matrix m_b
    if m_b == []:
        raise ValueError("m_b can't be empty")
    for row2 in m_b:
        if type(row2) != list:
            raise TypeError("m_b must be a list of lists")
        len2 = len(m_b[0])
        if row2 == []:
            raise ValueError("m_b can't be empty")
        if len2 != len(row2):
            raise TypeError("each row of m_b must be of the same size")
        num_row2 += 1
        for column2 in row2:
            if type(column2) != int and type(column2) != float:
                raise TypeError("m_b should contain only integers or floats")

    # Check if the multiplication is posible
    if num_colum1 != num_row2:
        raise ValueError("m_a and m_b can't be multiplied")

    mul_matrix = []

    for row_1 in m_a:
        l = 0
        l_row = []
        while l < len(m_b[0]):
            result = 0
            k = 0
            for column_1 in row_1:
                result += column_1 * m_b[k][l]
                k += 1
            l_row.append(result)
            l += 1
        mul_matrix.append(l_row)

    return mul_matrix
