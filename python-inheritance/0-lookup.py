#!/usr/bin/python3

'''0-lookup.py
This module contain a function that can list all the attributes and methods of
an object'''


def lookup(obj):
    '''This function return a list of method, and attributes an object can
    have'''

    class_attributes = dir(obj)

    return class_attributes
