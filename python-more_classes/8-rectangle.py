#!/usr/bin/python3

'''
8-rectangle.py

Initialization of the class Rectangle and all of its attributes and instances.
'''


class Rectangle:
    '''
    Initialization of the class Rectangle and all of its attributes
    '''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''First initialization of a new instance with the width and the height
        of the new rectangle'''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    @property
    def area(self):
        '''Return the area of the current rectangle'''
        return (self.__height * self.__width)

    def perimeter(self):
        '''Return the perimeter of the current rectangle'''
        if self.__height != 0 and self.__width != 0:
            return ((self.__height * 2) + (self.__width * 2))
        else:
            return 0

    def __str__(self):
        '''Return a string that represent the current rectangle'''
        rectangle_str = ""
        self.print_symbol = str(self.print_symbol)

        if self.__width == 0 or self.__height == 0:
            return (rectangle_str)
        else:
            for i in range(0, self.__height):
                for j in range(0, self.__width):
                    rectangle_str += self.print_symbol
                if i != self.__height - 1:
                    rectangle_str += "\n"
            return rectangle_str

    def __repr__(self):
        '''Return a new Rectangle with the arguments of the current
        rectangle'''
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        '''Print a sentence when an instance is delete'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        ''' Return the instance with the biggest area'''
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area > rect_2.area:
                return (rect_1)
            elif rect_1.area < rect_2.area:
                return (rect_2)
            else:
                return (rect_1)
