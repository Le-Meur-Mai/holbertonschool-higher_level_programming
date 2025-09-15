#!/usr/bin/python3

'''
3-square.py

Code that initialize the attributes of the class Square
'''


class Square:
    '''
    initialization of the class named Square, and all the instances of it
    '''
    def __init__(self, size=0, position=(0, 0)):
        '''
        initialization of the size and position in the argument of the class,
        wich defines the size of your square, if no size is entered, size = 0,
        and defines the position of your square, if no position is enteref,
        position = (0, 0)
        '''

        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

        if (
            type(position) is not tuple
            or len(position) != 2
            or position[0] < 0
            or position[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def size(self):
        '''
        Return the size of the square
        '''
        return (self.__size)

    @property
    def position(self):
        '''
        Return the position of the square
        '''
        return (self.__position)

    @position.setter
    def position(self, value):
        '''
        Modification of the position of the square, that verify if the argument
        is correct
        '''
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in value:
            if type(value[i]) is not int or type(value[i]) < 0:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
        Instance that print the current square with # at the position entered
        '''
        if self.__size == 0:
            print("")
        else:
            if self.position[1] > 0:
                for h in range(0, self.__position[1]):
                    print("")

            for i in range(0, self.__size):
                for j in range(0, self.__position[0]):
                    print("_", end="")
                print("#" * self.__size, end="")
                print("")
