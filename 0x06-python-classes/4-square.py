#!/usr/bin/python3
'''create class'''


class Square:
    '''init function'''

    def __init__(self, size=0):
        self.__size = size
        '''proprety'''

    @proprety
    def size(self):
        return (self.__size)
        '''setter'''

    @size.setter
    def size(self, value):
        if not type(value) is int:
            raise TypeError("size must be an integer")
        if value  < 0:
            raise ValueError("size must be >= 0")
        selfe.__size = value
        '''return the area'''

    def area(self):
        return (self.__size * self.__size)
