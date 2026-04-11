#!/usr/bin/python3
"""Square klasi ucun modul senedlesdirilmesi"""


class Square:
    """Kvadratı temsil eden klas"""

    def __init__(self, size=0):
        """Kvadratı ilkin deyerlerle yaradir

        Args:
            size (int): Kvadratin terefinin olcusu.
        """
        self.size = size

    @property
    def size(self):
        """Kvadratin olcusunu geri qaytarir (Getter)"""
        return self.__size

    @size.setter
    def size(self, value):
        """Kvadratin olcusunu teyin edir (Setter)

        Args:
            value (int): Yeni olcu deyeri.

        Raises:
            TypeError: Eger value integer deyilse.
            ValueError: Eger value 0-dan kicikdirse.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Kvadratin sahesini hesablayir ve qaytarir

        Returns:
            Kvadratin sahesi (int)
        """
        return self.__size ** 2
