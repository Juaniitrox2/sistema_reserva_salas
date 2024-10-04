"""
    Define la clase DateTime conteniendo una fecha (DD/MM/AAAA) y hora (HH/MM/SS)
"""

from Negocio.time import Time
from Negocio.date import Date


class DateTime:
    """Una fecha y hora de un año, mes y día especifico"""

    def __init__(self, year, month, day, hour, minute):
        self._date = Date(day, month, year)
        self._time = Time(hour, minute)

    def from_string(base_string: str) -> "DateTime":
        """
            Genera un DateTime en base a texto
        
            Args:
                base_string (str): La fecha en formato stringusando [YYYY/MM/DD - HH:MM]

            Returns:
                DateTime: Objeto datetime creado con los valores  de texto entregados
        """
        split = base_string.split(" - ")
        date = split[0].split("/")
        time = split[1].split(":")

        return DateTime(int(date[2]), int(date[1]), int(date[0]), int(time[0]), int(time[1]))

    def __str__(self) -> str:
        return f"{str(self._date)} - {str(self._time)}"

    def __eq__(self, other: "DateTime"):
        return self._date == other._date and self._time == other._time

    def __gt__(self, other: "DateTime"):
        return ((self._date > other._date) or (self._date == other._date and self._time > other._time))

    def __ge__(self, other: "DateTime"):
        return (self > other or self == other)

    def __hash__(self) -> int:
        return hash((self._date, self._time))
