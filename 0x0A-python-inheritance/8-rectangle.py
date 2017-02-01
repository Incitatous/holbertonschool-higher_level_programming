#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

b = BaseGeometry()
r = Rectangle(2, 1)
print(type(r))
print(isinstance(r, BaseGeometry))
print(type(b))
print(issubclass(Rectangle, BaseGeometry))
