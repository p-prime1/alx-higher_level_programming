#!/usr/bin/python3
import copy


def square_matrix_simple(matrix=[]):
    """Returns the square of all the numbers in a square matrix"""
    new_matrix = copy.deepcopy(matrix)
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[i])):
            new_matrix[i][j] = new_matrix[i][j] ** 2

    return (new_matrix)
