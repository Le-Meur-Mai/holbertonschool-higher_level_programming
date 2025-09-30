#!/usr/bin/python3

'''
10-student/py
Module that add the class student with all its attributes and methods
'''


class Student:
    '''Creating a class Student with all its attributes and methods'''

    def __init__(self, first_name, last_name, age):
        '''Initialization of the instance'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Adding a method that retrieve the dictionnary format of all
        the attributes of the instance or of the specified attributes'''
        if type(attrs) is list and len(attrs) > 0:
            new_dict = {}
            j = 0
            for i in attrs:
                if type(i) is str and i in self.__dict__:
                    new_dict[i] = self.__dict__[i]
                    j += 1
            if new_dict is {} or j == 0:
                return self.__dict__
            else:
                return new_dict
        else:
            return self.__dict__
