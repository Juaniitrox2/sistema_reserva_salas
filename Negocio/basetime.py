""" 
    Define la clase base tiempo, la cual determina una base sobre la cual funcionan todas las clases
    relacionadas al tiempo, desde Año hasta el Minuto
"""

class BaseTime:
    """Una cantidad de tiempo determinada"""

    def __init__(self, value: int) -> None:
        pass

    def __str__(self):
        """Muestra la cantidad de tiempo en formato texto"""

    def __gt__(self, other: "BaseTime") -> bool:
        """Compara si el tiempo es mayor a otro"""
        return self._value > other._value
    
    def __eq__(self, other: "BaseTime") -> bool:
        """Retorna un booleano indicando si el valor es igual en ambos casos"""
        return self._value == other._value
    
    def __hash__(self) -> int:
        return hash(self._value)