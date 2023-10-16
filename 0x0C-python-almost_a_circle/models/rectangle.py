#!/usr/bin/python3
"""traitement"""


from models.base import Base

class Rectangle(Base):
    '''class rectangle'''

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter of width'''
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''getter'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter'''
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''setter'''
        return self.__x

    @x.setter
    def x(self, value):
        '''seter'''
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''getter'''
        return self.__y

    @y.setter
    def y(self, value):
        '''setter'''
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''area'''
        return self.width * self.height

    def display(self):
        '''display'''
        for v in range(self.y):
            print('')
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        '''Update the Rectangle.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        '''
        lis = ["id", "width", "height", "x", "y"]
        if args:
            i = 0
            while i < len(args):
                setattr(self, lis[i], int(args[i]))
                i += 1
        else:
            for key in kwargs:
                if key in lis:
                    setattr(self, key, kwargs[key])

    def to_dictionary(self):
        '''Return the dictionary representation of a Rectangle.'''
        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}

    def __str__(self):
        '''Return the print() and str() representation of the Rectangle.'''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.x, self.y, self.width, self.height)
