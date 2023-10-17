#!/usr/bin/python3
'''traitement of square'''
from models.rectangle import Rectangle


class Square(Rectangle):
    """classs square"""

    def __init__(self, size, x=0, y=0, id=None):
        """init func"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """size"""
        return self.width

    @size.setter
    def size(self, value):
        """size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        lis = ["id", "size", "x", "y"]
        if args:
            i = 0
            while i < len(args):
                setattr(self, lis[i], args[i])
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''dect representation'''
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.x}

    def __str__(self):
        """string representation"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)
