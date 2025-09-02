#!/usr/bin/python3
import sys
if __name__ == "__main__":
    nb_of_arg = len(sys.argv) - 1
    if nb_of_arg != 1:
        print("{} arguments".format(nb_of_arg), end="")
    elif nb_of_arg == 1:
        print("{} argument".format(nb_of_arg), end="")
    if nb_of_arg == 0:
        print(".")
    else:
        print(":")

    for i in range(1, (len(sys.argv))):
        print("{}: {}".format(i, sys.argv[i]))
