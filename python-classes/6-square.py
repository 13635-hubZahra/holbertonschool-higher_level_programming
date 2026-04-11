i#!/usr/bin/python3
"""Square klasi ucun modul senedlesdirilmesi"""


class Square:
    """Kvadratı temsil eden klas"""

    def __init__(self, size=0, position=(0, 0)):
        """Kvadratı ilkin deyerlerle yaradir

        Args:
            size (int): Kvadratin terefinin olcusu.
            position (tuple): Kvadratin koordinatlari.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Kvadratin olcusunu geri qaytarir (Getter)"""
        return self.__size

    @size.setter
    def size(self, value):
        """Kvadratin olcusunu teyin edir (Setter)"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Kvadratin koordinatlarini geri qaytarir (Getter)"""
        return self.__position

    @position.setter
    def position(self, value):
        """Kvadratin koordinatlarini teyin edir (Setter)"""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Kvadratin sahesini hesablayir ve qaytarir"""
        return self.__size ** 2

    def my_print(self):
        """Kvadratı # simvollari ve bosluqlarla ekrana cap edir"""
        if self.__size == 0:
            print("")
            return

        # Yuxari bosluqlar (position[1])
        if self.__size > 0:
            for y in range(self.__position[1]):
                print("")

        # Kvadratin ozu ve sol bosluqlar (position[0])
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
