#!/usr/bin/python3

import random
while (1):
    number = random.randint(0, 100)
    print ("Sélectionnez votre difficulté : 'ez', 'med' 'dif'")
    difficulty = input()
    while difficulty != "ez" and difficulty != 'med' and difficulty != 'dif':
         print("Difficulté non valide, réessayez 'ez', 'med', 'dif'")
         difficulty = input()
    i = 1
    if difficulty == "ez":
         limit = 15
    elif difficulty == "med":
         limit = 10
    else:
         limit = 5
    print("Try to guess the number :")
    guess = input()
    while (1):
        while (not guess.isnumeric() or int(guess) < 0 or int(guess) > 100):
            print("Ce n'est pas un nombre, ou il n'est pas compris entre " \
            "et 100 réessayez : ", end="")
            guess = input()
        guess = int(guess)
        if guess < number:
            print(f"{guess} est trop petit, réessayez :")
        elif guess > number:
            print(f"{guess} est trop grand, réessayez :")
        elif guess == number:
             print(f"Bravo le nombre secret était bien {number}!")
             print(f"Vous avez mis {i} essai(s)")
             break
        guess = input()
        i += 1
        if limit < i:
             print(f"Vous n'avez pas réussi à trouver {number} dans le " \
             "nombre d'essais impartis")
             break
    print("Voulez-vous rejouer, y ou n : ", end="")
    replay = input()
    while (replay != "y" and replay != "n"):
            print("Réponse non valide, recommencez: y ou n : ", end="")
            replay = input()
    if replay == "n":
        print("C'est tchaow")
        exit()
