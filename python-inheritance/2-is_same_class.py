#!/usr/bin/python3
'''2-is_same_class.py
Add a function that return True if the object enter is an instance of the
exact class'''


def is_same_class(obj, a_class):
    '''Creating a function that tell you if the object enter is an instance of
    the exact class'''

    if type(obj) is a_class:
        return True
    else:
        return False
