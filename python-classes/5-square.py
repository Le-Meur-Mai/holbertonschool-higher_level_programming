#!/usr/bin/python3

'''
3-square.py

Code that initialize the attributes of the class Square
'''


class Square:
    '''
    initialization of the class named Square, and all the instances of it
    '''
    def __init__(self, size=0):
        '''
        initialization of the size in the argument of the class, wich defines
        the size of your square, if no size is entered, size = 0
        '''

        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def size(self):
        '''
        Return the size of the square
        '''
        return (self.__size)

    @size.setter
    def size(self, value):
        '''
        Modification of the size of the square, that verify if the argument is
        correct.
        '''
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        '''
        Instance that return the area of the square
        '''
        return (self.__size * self.__size)

    def my_print(self):
        '''
        Instance that print the current square with #
        '''
        for i in range(0, self.__size):
            print("#" * self.__size, end="")
            print("")
        if self.__size == 0:
            print("")
