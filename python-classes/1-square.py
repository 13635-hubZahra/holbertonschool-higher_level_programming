#!/usr/bin/python3
"""Square klasi ucun modul senedlesdirilmesi"""


class Square:
    """Kvadratı temsil eden klas"""

    def __init__(self, size):
        """Kvadratı ilkin deyerlerle yaradir

        Args:
            size: Kvadratin terefinin olcusu
        """
        self.__size = size
