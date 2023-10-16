#!/usr/bin/python3
'''traitement of square'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''class square'''

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width
        return self.height

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        lis = ["id", "size", "x", "y"]
        if args:
            i = 0
            while i < len(args):
                setattr(self, lis[i], int(args[i]))
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.x}

     
    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.width)
