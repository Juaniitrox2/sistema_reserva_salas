""" 
    Define la clase Segundo, que funciona como base para el resto de las clases de horario
"""

class Second:
    """Una cantidad determinada de segundos"""

    def __init__(self, amount: int) -> None:
        self.__amount = amount

    def __len__(self) -> None:
        return self.__amount
