#!/usr/bin/python3
"""this is my class"""


class Rectangle:
    "element of my class"""
    number_of_instances = 0
    print_symbol = "#" 

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int):
            self.__width = value
        else:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            self.__height = value
        else:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        return int(self.__width) * (self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return int(((self.__width) + (self.__height)) * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return("")
        else:
            rect = ""
            for i in range(self.__height):
                for j in range(self.__width):
                    rect += str(self.print_symbol)
                rect += "\n"
            return rect[:-1]

    def __repr__(self):
        "creat a new object using evel()"
        rect = f"Rectangle({self.width}, {self.height})"
        return (rect)

    def __del__(self):
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1
        print("Bye rectangle...")
