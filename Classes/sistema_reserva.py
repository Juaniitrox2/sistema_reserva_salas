"""
    Define la clase Sala y la clase Sistema de Reservas

"""

from Classes.interval import Interval
from Classes.exceptions import InvalidRoom

class Room:
    """Una sala con un proposito único"""
    def __init__(self, name: str, maximum_capacity: int) -> None:
        self.__name = name
        self.__bookings: list[Interval] = []
        self.__maximum_capacity = maximum_capacity

    @property
    def room_name(self):
        """Retorna el nombre de la sala"""
        return self.__name

    @property
    def capacity(self):
        return self.__maximum_capacity

    def book(self, interval: Interval):
        self.__bookings.append(interval)

    def is_occupied_on(self, interval: Interval) -> bool:
        """Retorna un booleano indicando si la fecha está dentro de una reserva"""

        for date in self.__bookings:
            if date.overlaps_with(interval):
                return True
        return False

class BookingSystem:
    def __init__(self):
        self.__salas = {}

    def add_room(self, room: Room):
        """Agrega una sala al sistema"""
        self.__salas[room.room_name] = Room

    def book_room(self, room_name: str, date_interval: Interval):
        """Reserva una sala en el sistema"""
        if not self.__salas[room_name]:
            raise InvalidRoom("Sala inexistente")

        if self.__salas[room_name].is_occupied_on(date_interval):
            raise InvalidRoom("La sala está ocupada en el horario solicitado")

        self.__salas[room_name].book(date_interval)
