#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        strng = ""
        for z in x:
            strng += "{:d} ".format(z)
        print("{}".format(strng[:-1]))
