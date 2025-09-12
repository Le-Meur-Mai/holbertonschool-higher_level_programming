"""
0-add_integer.py

Ce module permet de fornir une fonction qui permet de faire des additions
de manière sécurisée.
"""


def add_integer(a, b=98):
    """
    Calcule la somme de deux nombres entiers.
    Si un des nombres n'est pas un entier, il sera converti en tant que tel.
    L'argument b rajoute 98 au nombre passé en argument.

    Args:
    a: le premier nombre de type int ou float
    b: le premier nombre de type int ou float

    return: a + b
    """
    try:
        if type(a) is float:
            a = int(a)
        if type(b) is float:
            b = int(b)
        result = a + b
        return (result)
    except TypeError:
        if not isinstance(a, (int, float)):
            raise TypeError("a must be an integer")
        else:
            raise TypeError("b must be an integer")
    except OverflowError:
        raise OverflowError("Float too big to convert to int for the system")
