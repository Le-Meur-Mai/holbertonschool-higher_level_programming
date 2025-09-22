#!/usr/bin/python3
'''8-base_geometry.py
Module that contain an empty class'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Creating a subclass of BasicGeometry'''
    def __init__(self, width, height):
        '''Initialization of the arguments'''
        if self.integer_validator("width", width) is True:
            self.__width = width
        if self.integer_validator("height", height) is True:
            self.__height = height

    def __str__(self):
        value_printed = "[Rectangle] "
        value_printed += str(self.__width)
        value_printed += "/"
        value_printed += str(self.__height)
        return value_printed
    
    def area(self):
        area_value = self.__width * self.__height
        return area_value
