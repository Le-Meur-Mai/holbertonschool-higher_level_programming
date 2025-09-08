#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if len(matrix) > 0:
        new_matrix = [row[:] for row in matrix]
        for i in range(0, len(new_matrix)):
            for j in range(0, len(new_matrix[i])):
                new_matrix[i][j] *= new_matrix[i][j]

        return (new_matrix)
