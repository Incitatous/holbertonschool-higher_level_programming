#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        myError = "position must be a tuple of 2 positive integers"
        if type(position) is not tuple and len(position) is not 2:
            if position[0] < 0 and position[1] < 0:
                raise TypeError(myError)
        self.__position = position

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            for j in range(self.__size):
                print("#", end="")
            print("")
