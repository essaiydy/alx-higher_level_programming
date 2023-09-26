#!/usr/bin/python3
'''creat a class'''


class Square:
    '''the __init__ function'''

    size: def __init__(self, size=0):
        if type(size) is int:
            if size > 0:
                self.__size = size
            else:
                raise TypeError("size must be an integer")
        else:
            raise ValueError("size must be >= 0")
            '''return the area'''

        def area(self):
            return (self.__size * self.__size)
