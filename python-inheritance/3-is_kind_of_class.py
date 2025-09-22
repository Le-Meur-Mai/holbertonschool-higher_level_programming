#!/usr/bin/python3
'''3-is_kind_of_class.py
Add a function that return True if the object enter is an instance of the
class entered'''


def is_kind_of_class(obj, a_class):
    '''Creating a function that tell you if the object enter is an instance of
    the class entered'''

    if isinstance(obj, a_class):
        return True
    else:
        return False
