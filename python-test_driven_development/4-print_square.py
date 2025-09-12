#!/usr/bin/python3

'''
4-print_square.py

Ce module permet de fournir une fonction qui vous affiche des carrés de #
suivant un nombre rentré en argument.
'''

def print_square(size):
    '''
    Fonction qui affiche des carrés de # suivant une taille donnée en argument.

    Arg:
    size: un nombre positif de type int

    return: None
    '''

    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(0, size):
        print("#" * size, end="")
        print("")
