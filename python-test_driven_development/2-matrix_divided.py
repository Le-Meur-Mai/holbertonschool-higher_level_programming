#!/usr/bin/python3

'''
2-matrix_divided.py

Ce module permet de fournir une fonction qui divise tous les nombres d'une
matrice par un nombre passé en argument
'''


def matrix_divided(matrix, div):
    '''
    Calcule à deux décimales près la division de chaque nombres dans la matrice
    avec un nombre rentré en argument.

    Args:
    matrix: La matrice dont les valeurs sont à diviser.
    div: Un int ou float qui est le diviseur.

    return: result, une nouvelle matrice qui a pour valeur les résultats des
    divisions.
    '''

    if not isinstance(matrix, list):
        raise TypeError(
                        "matrix must be a matrix (list of lists) "
                        "of integers/floats")

    if len(matrix) < 1:
        raise IndexError("matrix must not be empty")

    for row in matrix:
        if len(matrix[0]) != len(row):
            raise TypeError(
                "Each row of the matrix must have the same size")

    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], (float, int)):
                raise TypeError(
                                "matrix must be a matrix (list of lists) "
                                "of integers/floats")

    try:
        result = []
        for i in range(len(matrix)):
            result.append(matrix[i][:])

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                result[i][j] = round(matrix[i][j] / div, 2)

        return (result)

    except OverflowError:
        raise OverflowError("Float too big for the system")

    except ZeroDivisionError:
        raise ZeroDivisionError("division by zero")
