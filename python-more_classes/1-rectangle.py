#!/usr/bin/python3

'''
1-rectangle.py

Initialization of the class Rectangle and all of its attributes and instances.
'''


class Rectangle:
    '''
    Initialization of the class Rectangle and all of its attributes
    '''

    def __init__(self, width=0, height=0):
        '''First initialization of a new instance with the width and the height
        of the new rectangle'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Retrieve the attribute width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Verification of the value entered in the argument width'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''Retrieve the attribute height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Verification of the value entered in the argument height'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
