#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    sq_matrix = []
    for row in new_matrix:
        inner_matrix = []
        for i in row:
            inner_matrix.append( i * i)
        sq_matrix.append(inner_matrix)
    return sq_matrix
