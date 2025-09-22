#!/usr/bin/python3
'''4-inherits_from.py
Adding a function that return True if the object is a subclass of the
class entered'''


def inherits_from(obj, a_class):
    '''Function that return True if the object is a subclass of the class
    entered'''
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
