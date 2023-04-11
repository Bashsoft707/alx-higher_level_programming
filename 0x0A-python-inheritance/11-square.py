#!/usr/bin/python3
"""module to define class Square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""

    def __init__(self, size):
        """initializes a Square instance"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """returns the string representation of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)

