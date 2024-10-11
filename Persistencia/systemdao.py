"""Define la clase de BookingSystemDAO"""
import sqlite3

from Negocio.system import BookingSystem, Room
from Negocio.interval import Interval
from Negocio.exceptions import InvalidRoom, OccupiedRoom
from Negocio.datetime import DateTime
from Persistencia.systemdaointerface import SystemDaoInterface

class SQLBookingSystem(SystemDaoInterface):
    def __init__(self, system: BookingSystem, path: str) -> None:
        self.__db_path = path
        self.__system = system
        self.__create_table()

    def __create_table(self) -> None:
        with sqlite3.connect(self.__db_path) as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS reservas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    sala_nombre INTEGER NOT NULL,
                    inicio TEXT NOT NULL,
                    fin TEXT NOT NULL,
                    FOREIGN KEY (sala_nombre) REFERENCES salas(nombre)
                )"""
            )

    def add_booking(self, room: str, booking: Interval):
        try:  
            reserved_room = self.__system.book_room(room, booking)

            print(reserved_room)
            with sqlite3.connect(self.__db_path) as connection:
                connection.execute(
                    "INSERT INTO reservas (sala_nombre, inicio, fin) VALUES (?, ?, ?)",
                    (room, str(booking.start), str(booking.end)),
                )
        except OccupiedRoom:
            print("Sala ya ocupada en esa fecha")

    def show_bookings(self, room_name: str) -> list[Interval]:
        with sqlite3.connect(self.__db_path) as connection:
            cursor = connection.execute(
                "SELECT inicio, fin FROM reservas WHERE sala_nombre = ?",
                (room_name,),
            )

            bookings = cursor.fetchall()

        return [
            Interval(starting_date=DateTime.from_string(row[0]), ending_date=DateTime.from_string(row[1])) for row in bookings
        ]
    
    def remove_booking(self, room_name: str, interval: Interval) -> None:
        try:
            self.__system.remove_booking(room_name, interval)

            with sqlite3.connect(self.__db_path) as connection:
                connection.execute(
                    "DELETE FROM reservas WHERE sala_nombre = ? and inicio = ? and fin = ?",
                    (room_name, str(interval.start), str(interval.end))
                )
        except:
            print("que ha salido mal macho")

    def get_rooms(self) -> list[Room]:
        return self.__system.available_rooms()
            
class JSONBookingSystem(SystemDaoInterface):
    def __init__(self):
        pass