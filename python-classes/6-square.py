#!/usr/bin/python3
"""Square klasi ucun modul senedlesdirilmesi"""


class Square:
    """Kvadratı temsil eden klas"""

    def __init__(self, size=0, position=(0, 0)):
        """Kvadratı ilkin deyerlerle yaradir"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Olculeri geri qaytarir"""
        return self.__size

    @size.setter
    def size(self, value):
        """Olculeri teyin edir"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Koordinatlari geri qaytarir"""
        return self.__position

    @position.setter
    def position(self, value):
        """Koordinatlari teyin edir"""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Saheni hesablayir"""
        return self.__size ** 2

    def my_print(self):
        """Kvadratı koordinatlara uygun cap edir"""
        if self.__size == 0:
            print("")
            return

        for i in range(self.__position[1]):
            print("")

        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
