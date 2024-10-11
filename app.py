"""
    Define las funciones y rutas para la página/app de Flask
    Implementa el sistema de reservas creado orientado a objetos
"""

from flask import Flask,render_template,request
from Negocio.system import BookingSystem, Room
from Persistencia.systemdao import SQLBookingSystem, JSONBookingSystem
from Negocio.interval import Interval
from Negocio.datetime import DateTime

app=Flask(__name__)

def crear_sistema():
    """Inicializa el programa principal"""
    sistema = BookingSystem()

    sistema.add_room(Room("Sala 1", 15))
    sistema.add_room(Room("Sala 2", 15))
    sistema.add_room(Room("Sala 3", 15))

    daoSystem = SQLBookingSystem(sistema, "reservas.db")

    #daoSystem.add_booking("Sala 1", Interval(DateTime(2024, 1, 1, 0, 0), DateTime(2024, 1, 1, 6, 0)))
    #daoSystem.add_booking("Sala 1", Interval(DateTime(2024, 2, 20, 0, 0), DateTime(2024, 2, 20, 18, 0)))
    #daoSystem.add_booking("Sala 2", Interval(DateTime(2024, 11, 22, 0, 0), DateTime(2024, 11, 23, 0, 0))) #pylint: disable=C0301
    #daoSystem.add_booking("Sala 3", Interval(DateTime(2024, 11, 16, 0, 0), DateTime(2024, 11, 16, 19, 0))) #pylint: disable=C0301

    #daoSystem.add_booking("Sala 3", Interval(DateTime(2024, 7, 18, 0, 0), DateTime(2024, 7, 18, 1, 0)))

    return daoSystem

sistema_reservas = crear_sistema()

def obtener_reservas():
    """Devuelve una lista de todas las reservas actuales en la página"""
    reservas = []

    id_reserva = 0
    for sala in sistema_reservas.get_rooms():
        for reserva in sistema_reservas.show_bookings(sala):
            id_reserva += 1
            reservas.append((id_reserva, sala, reserva.start, reserva.end))

    return reservas

def agregar_reserva(room: str, start, end):
    """Agrega una reserva a una habitación"""
    booking_interval = Interval(start, end)

    sistema_reservas.add_booking(room, booking_interval)

def cancelar_reserva(id_booking: int):
    """Cancela una reserva para una habitación"""

    total = obtener_reservas()
    for booking in total:
        print(booking[0], id_booking)
        if booking[0] == id_booking:
            time_interval = Interval(booking[2], booking[3])
            room = booking[1]

            sistema_reservas.remove_booking(room, time_interval)


def form_to_datetime(form):
    """Transforma un form a datetime usando los int"""
    start = DateTime(int(form["start_year"]), int(form["start_month"]),
                     int(form["start_day"]), int(form["start_hour"]), int(form["start_minute"]))
    end = DateTime(int(form["end_year"]), int(form["end_month"]),
                   int(form["end_day"]), int(form["end_hour"]), int(form["end_minute"]))

    return start, end

@app.route('/',methods=['GET','POST'])
def home():
    """Maneja la página principal, ruta / de la página"""
    if request.method=='POST':
        return render_template('index.html')

    return render_template('index.html', reservas=obtener_reservas())

@app.route('/reservar', methods=['GET', 'POST'])
def reservar():
    """Maneja la ruta /reservar de la página"""
    if request.method == "POST":
        form = request.form
        start, end = form_to_datetime(form)

        agregar_reserva(form["sala"], start, end)


    return render_template("reservas.html", salas=sistema_reservas.get_rooms())

@app.route('/cancelar', methods=['GET', 'POST'])
def cancelar():
    """Controla la ruta /cancelar de la página"""
    if request.method == "POST":
        form = request.form
        booking = form.get("reserva")

        id_reserva = int(booking[1])
        cancelar_reserva(id_reserva)


    return render_template("cancelar.html", reservas=obtener_reservas())

if __name__ == '__main__':
    app.run(port=5000,debug=True)
