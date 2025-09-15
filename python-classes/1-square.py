#!/usr/bin/python3

'''
1-square.py

Code that initialize the attributes of the class Square
'''


class Square:
    '''
    initialization of the class named Square, and all the instances of it
    '''
    def __init__(self, size):
        '''
        initialization of the size in the argument of the class, wich defines
        the size of your square
        '''
        self.__size = size
