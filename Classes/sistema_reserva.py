"""
    Define la clase Sala y la clase Sistema de Reservas

"""

class Sala:
    """Una sala con un proposito único"""
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__reservas = []

    @property
    def nombre(self):
        """Retorna el nombre de la sala"""
        return self.__name

class SistemaReservas:
    def __init__(self):
        self.__salas = {}
