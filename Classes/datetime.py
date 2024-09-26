"""
    Define la clase DateTime conteniendo una fecha (DD/MM/AAAA) y hora (HH/MM/SS)
"""

from Classes.time import Time
from Classes.date import Date


class DateTime:
    """Una fecha y hora de un año, mes y día especifico"""

    def __init__(self, year, month, day, hour, minute):
        self._date = Date(day, month, year)
        self._time = Time(hour, minute)

    def __str__(self) -> str:
        return f"{str(self._date)} - {str(self._time)}"

    def __eq__(self, other):
        return self._date == other._date and self._time == other._time

    def __gt__(self, other):
        return self._date > other._date or (self._date == other._date and self._time > other._time)
