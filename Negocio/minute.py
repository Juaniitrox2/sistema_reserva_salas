"""
    Define la clase minuto:
        - No puede ser mayor a 59 o menor a 0
        - Tiene que ser un integer
"""

from Negocio.basetime import BaseTime
from Negocio.exceptions import InvalidDateValue

class Minute(BaseTime):
    """Un minuto de una hora"""

    def __init__(self, value: int) -> None:
        if value < 0 or value > 59:
            raise InvalidDateValue("Minuto inválido")

        self._value = value

    def __str__(self) -> str:
        return str(self._value)
