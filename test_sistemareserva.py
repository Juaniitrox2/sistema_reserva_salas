#pylint: skip-file
import unittest

from Classes.datetime import DateTime
from Classes.interval import Interval
from Classes.system import Room, BookingSystem
from Classes.exceptions import InvalidRoom

class TestDate(unittest.TestCase):
    def test_reserva_se_pisa_con_otra(self):
        f1 = Interval(DateTime(2024, 11, 23, 19, 00), DateTime(2024, 11, 24, 00, 00))   
        f2 = Interval(DateTime(2024, 11, 23, 21, 00), DateTime(2024, 11, 24, 2, 00))

        sala1 = Room("Sala Skibidi Dopdop", 15)
        sistema = BookingSystem()

        sistema.add_room(sala1)
        sistema.book_room("Sala Skibidi Dopdop", f1)

        with self.assertRaises(InvalidRoom):
            sistema.book_room("Sala Skibidi Dopdop", f2)

    def test_reservas_en_día(self):
        f1 = Interval(DateTime(2024, 11, 23, 19, 00), DateTime(2024, 11, 24, 00, 00))

        sala1 = Room("Sala 1", 15)
        sistema = BookingSystem()

        sistema.add_room(sala1)
        sistema.book_room("Sala 1", f1)

        sistema.get_bookings_for_day(DateTime(2024, 11, 23, 23, 00))

if __name__ == "__main__":
    unittest.main() 