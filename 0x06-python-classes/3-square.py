#!/usr/bin/python3
'''creat a class'''


class Square:
    '''the __init__ function'''

    def __init__(self, size=0):
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        '''return the area'''

    def area(self):
        return (self.__size * self.__size)
