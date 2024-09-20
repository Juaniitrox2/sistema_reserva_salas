"""
    Define la clase DateTime conteniendo una fecha (DD/MM/AAAA) y hora (HH/MM/SS)
"""


class DateTime:
    """Una fecha y hora de un año, mes y día especifico"""

    def __init__(self, date, time):
        self.__date = date
        self.__time = time

    def __str__(self) -> str:
        return f"{str(self.__date)} - {str(self.__time)}"
