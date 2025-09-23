#!/usr/bin/python3
'''10-square.py
Module that contain the subclass square'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Creating the subclass of rectangle: square'''
    def __init__(self, size):
        '''Initialization of the size'''
        if self.integer_validator("size", size) is True:
            self.__size = size

    def area(self):
        '''Calculate the area of the square'''
        return self.__size * self.__size

    def __str__(self):
        '''Print format of the square'''
        value_printed = "[Rectangle] "
        value_printed += str(self.__size)
        value_printed += "/"
        value_printed += str(self.__size)
        return value_printed
