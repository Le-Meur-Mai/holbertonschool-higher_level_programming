#!/usr/bin/python3
i = 0
j = 1
k = 1
while i < 9:
    while j <=9:
        if i != 8:
            print("{}{}, ".format(i, j), end="")
        else:
            print("{}{}".format(i,j))
        j += 1
    i += 1
    k += 1
    j = k
