#!/usr/bin/python3
"""Square klasi ucun modul senedlesdirilmesi"""


class Square:
    """Kvadratı temsil eden klas"""

    def __init__(self, size=0):
        """Kvadratı ilkin deyerlerle yaradir

        Args:
            size (int): Kvadratin terefinin olcusu. Standart deyer 0-dir.

        Raises:
            TypeError: Eger size integer deyilse.
            ValueError: Eger size 0-dan kicikdirse.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Kvadratin sahesini hesablayir ve qaytarir

        Returns:
            Kvadratin sahesi (int)
        """
        return self.__size ** 2
