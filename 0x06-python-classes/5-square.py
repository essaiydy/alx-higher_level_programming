#!/usr/bin/python3
'''class sqaur'''


class Square:
    '''the init func'''
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        '''return size'''
        return(self.__size)

    @size.setter
    def size(self, value):
        if not type(value) is int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        '''return the area'''

    def area(self):
        '''count area'''
        return (self.__size * self.__size)

    def my_print(self):
        '''print an squal using #'''
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print("")
