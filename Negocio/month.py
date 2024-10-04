"""
    Define la clase mes:
        - No puede ser mayor a 12 o menor a 0
        - Tiene que ser un integer
"""

from Negocio.basetime import BaseTime
from Negocio.exceptions import InvalidDateValue

class Month(BaseTime):
    """Un mes de un año"""

    def __init__(self, value: int) -> None:
        if value < 1 or value > 12:
            raise InvalidDateValue("Mes invalido")

        self._value = value

    def __str__(self) -> str:
        return str(self._value)
