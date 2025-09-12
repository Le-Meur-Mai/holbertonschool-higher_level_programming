#!/usr/bin/python3

'''
Ce module permet de forunir une fonction qui indente le texte correctement en
sautant deux lignes après certains caractères spéciaux
'''


def text_indentation(text):
    '''
    Cette fonction permet d'afficher et d'indenter un texte correctement en
    sautant deux lignes après certains caractères spéciaux comme :, ., ?

    Arg:
    text: Texte à indenter, ce doit être une chaîne de caractères

    return: None
    '''

    if type(text) is not str:
        raise TypeError("text must be a string")

    special_char = ['?', '.', ':']
    i = 0

    while i < len(text) and text[i] == " ":
        i += 1

    letter = i
    while letter < len(text):
        print(text[letter], end="")
        if text[letter] in special_char:
            print("\n")
            while letter < (len(text) - 1) and text[letter + 1] == " ":
                letter += 1
        letter += 1
