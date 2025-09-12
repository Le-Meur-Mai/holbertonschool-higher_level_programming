#!/usr/bin/pyhthon3

'''
3-say_my_name.py

Ce module permet de fournir une fonction qui affiche votre prénom et
nom de famille.
'''


def say_my_name(first_name, last_name=""):

    '''
    Fonction qui affiche my name is <ton prénom> <ton nom de famille>

    Args:
    first_name: une chaine de caractères contenant ton prénom
    last_name: une chaine de caractères contenant ton nom de famille

    return: None
    '''
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")

    if len(first_name) == 0 or len(last_name) == 0:
        raise TypeError("Strings must have at least one character")

    print("My name is {} {}".format(first_name, last_name))
