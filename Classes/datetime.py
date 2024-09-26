"""
    Define la clase DateTime conteniendo una fecha (DD/MM/AAAA) y hora (HH/MM/SS)
"""

from Classes.time import Time
from Classes.date import Date


class DateTime:
    """Una fecha y hora de un año, mes y día especifico"""

    def __init__(self, year, month, day, hour, minute):
        self.__date = Date(day, month, year)
        self.__time = Time(hour, minute)

    def __str__(self) -> str:
        return f"{str(self.__date)} - {str(self.__time)}"
