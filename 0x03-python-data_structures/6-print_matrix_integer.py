#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for ele in row:
            print("{:d}".format(element), end=' ' if ele != row[-1] else '')
        print()
