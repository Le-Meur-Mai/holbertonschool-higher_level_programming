#!/usr/bin/python3
'''Module that add a function that can read a file'''


def read_file(filename=""):
    # function that open and read a file
    with open(filename, "r", encoding='utf-8') as file:
        content = file.read()
        print(content)
