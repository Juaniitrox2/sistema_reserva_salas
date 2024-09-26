"""
    Define la clase día.
        - No puede ser un día mayor al 31 o menor al 1
        - Solo puede ser un int
"""

from Classes.basetime import BaseTime
from Classes.exceptions import InvalidDateValue

class Day(BaseTime):
    """Un día de un mes"""

    def __init__(self, value: int) -> None:
        if value < 1 or value > 31:
            raise InvalidDateValue("Día invalido")

        self._value = value

    def __str__(self):
        return str(self._value)
