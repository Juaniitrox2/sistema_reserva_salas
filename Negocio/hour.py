"""
    Define la clase Hora
        - No puede ser mas de 23 o menos de 0
        - Solo puede ser un integer
"""

from Negocio.basetime import BaseTime
from Negocio.exceptions import InvalidDateValue

class Hour(BaseTime):
    """Una hora del día"""

    def __init__(self, value: int) -> None:
        if value < 0 or value > 23:
            raise InvalidDateValue("Hora inválida")

        self._value = value

    def __str__(self):
        return str(self._value)
