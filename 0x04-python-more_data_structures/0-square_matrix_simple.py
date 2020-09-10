#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    list_new = []
    for row in matrix:
        list_new.append([n * n for n in row])
    return list_new
