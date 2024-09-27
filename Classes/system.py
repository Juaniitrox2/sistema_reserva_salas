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
        """Retorna la capacidad de la sala"""
        return self.__maximum_capacity

    def book(self, interval: Interval):
        """Reserva la sala por un periodo de tiempo específico"""
        self.__bookings.append(interval)

    def is_occupied_on(self, interval: Interval) -> bool:
        """Retorna un booleano indicando si la fecha está dentro de una reserva"""

        for date in self.__bookings:
            if date.overlaps_with(interval):
                print(date)
                return True
    
        return False

    def remove_booking(self, interval: Interval):
        """Remueve una reserva de la sala"""

        if interval in self.__bookings:
            self.__bookings.remove(interval)

    def has_booking_on_date(self, date) -> bool:
        """Devuelve si la fecha está dentro de las reservas de la sala"""
        total = [str(interval) for interval in self.__bookings if interval.contains_date(date)]

        return total

    def get_bookings(self) -> list[Interval]:
        """Devuelve todas las reservas en la sala"""
        return self.__bookings

class BookingSystem:
    """Un sistema de reservas"""
    def __init__(self):
        self.__rooms = {}

    def add_room(self, room: Room):
        """Agrega una sala al sistema"""
        self.__rooms[room.room_name] = room

    def book_room(self, room_name: str, date_interval: Interval):
        """Reserva una sala en el sistema"""
        self.__verify_room(room_name)
        if self.get_room(room_name).is_occupied_on(date_interval):
            raise InvalidRoom("La sala está ocupada en el horario solicitado")

        self.get_room(room_name).book(date_interval)

    def get_room(self, room_name: str) -> Room:
        """Retorna una sala en base a su nombre"""
        return self.__rooms[room_name]

    def remove_booking(self, room_name: str, booking_interval: Interval):
        """Elimina una reserva de una sala"""
        self.__verify_room(room_name)
        self.get_room(room_name).remove_booking(booking_interval)

    def get_bookings_for_day(self, date):
        """Devuelve todas las reservas que incluyen al día"""
        bookings = [(room.room_name, room.has_booking_on_date(date)) 
                    for room in self.__rooms.values() if len(room.has_booking_on_date(date)) > 0]

        return bookings

    def available_rooms(self) -> list[str]:
        """Devuelve todas las salas disponibles"""
        return [room for room in self.__rooms]

    def get_room_bookings(self, room: str) -> list[Interval]:
        """Devuelve todas las reservas para esa sala"""

        self.__verify_room(room)
        return self.get_room(room).get_bookings()

    def __verify_room(self, room_name: str):
        """Valida si la sala existe y si no, levanta una excepción"""
        if not self.get_room(room_name):
            raise InvalidRoom("Sala inexistente")
