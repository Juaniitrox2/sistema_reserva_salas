""" 
    Define la clase abstracta tiempo, la cual determina una base sobre la cual funciona
"""

from abc import ABC

class BaseTime(ABC):
    """Una cantidad de tiempo determinada"""

    def __init__(self, value: int) -> None:
        pass

    def __str__(self):
        """Muestra la cantidad de tiempo en formato"""
