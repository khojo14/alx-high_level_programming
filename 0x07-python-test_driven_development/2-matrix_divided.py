#!/usr/bin/python3
"""
This is the 2-matrix_divided module

This module supplies one function, matrix_divided().
"""


def matrix_divided(matrix, div):
    """Divides all elements in the matrix with a number."""
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    size = len(matrix[0])
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if type(element) is not int:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) is not int or type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    result_matrix = [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
    return result_matrix
