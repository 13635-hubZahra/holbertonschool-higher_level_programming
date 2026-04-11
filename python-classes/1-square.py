#!/usr/bin/python3
"""Square klasınıemsil eden  modul"""


class Square:
    """Kvadratı emsil eden klas"""

    def __init__(self, size):
        """Kvadratı ilkin eyerlerle yaradir

        Args:
            size (int): Kvadratınterefinin ölç�.
        """
        self.__size = size
