#pylint: skip-file
import unittest

from Negocio.datetime import DateTime
from Negocio.interval import Interval
from Negocio.system import Room, BookingSystem
from Negocio.exceptions import InvalidRoom

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

        res = sistema.get_bookings_for_day(DateTime(2024, 11, 23, 23, 00))
        self.assertEqual([("Sala 1", ["23/11/2024 - 19:00 | 24/11/2024 - 00:00"])], res)

    def test_reserva_se_cancela(self):
        f1 = Interval(DateTime(2024, 11, 23, 19, 00), DateTime(2024, 11, 24, 00, 00))

        sala1 = Room("Sala 1", 15)
        sistema = BookingSystem()

        sistema.add_room(sala1)
        sistema.book_room("Sala 1", f1)
        sistema.remove_booking("Sala 1", f1)

        res = sistema.get_bookings_for_day(DateTime(2024, 11, 23, 23, 00))
        self.assertEqual([], res)

    def test_reserva_se_cancela_con_misma_fecha_distinto_objeto(self):
        f1 = Interval(DateTime(2024, 11, 23, 19, 00), DateTime(2024, 11, 24, 00, 00))
        f2 = Interval(DateTime(2024, 11, 23, 19, 00), DateTime(2024, 11, 24, 00, 00))

        sala1 = Room("Sala 1", 15)
        sistema = BookingSystem()

        sistema.add_room(sala1)
        sistema.book_room("Sala 1", f1)
        sistema.remove_booking("Sala 1", f2)

        res = sistema.get_bookings_for_day(DateTime(2024, 11, 23, 23, 00))
        self.assertEqual([], res)

    def test_sistema_muestra_salas_disponibles_correctamente(self):
        s1 = Room("S1", 3)
        s2 = Room("S2", 5)

        sys = BookingSystem()
        sys.add_room(s1)
        sys.add_room(s2)

        self.assertEqual(["S1", "S2"], sys.available_rooms())


if __name__ == "__main__":
    unittest.main() 