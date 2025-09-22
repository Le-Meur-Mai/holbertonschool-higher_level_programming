#!/usr/bin/python3
'''1-my_list.py
Adding a class MyList that can print the value of a list in ascending order'''


class MyList(list):
    '''Creation of a class that inherite from the class list'''

    def print_sorted(self):
        '''Method that print the elements of a list in ascending order'''

        return (sorted(self))
