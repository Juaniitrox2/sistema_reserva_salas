from flask import Flask,redirect,url_for,render_template,request
from Classes.system import BookingSystem, Room
from Classes.interval import Interval
from Classes.datetime import DateTime

app=Flask(__name__)

def crear_sistema():
    sistema = BookingSystem()
    sistema.add_room(Room("Sala 1", 15))
    sistema.add_room(Room("Sala 2", 15))
    sistema.add_room(Room("Sala 3", 15))

    #TODO: Agregar salas y reservas acá

    sistema.book_room("Sala 1", Interval(DateTime(2024, 1, 1, 0, 0), DateTime(2024, 1, 1, 6, 0)))
    
    return sistema

sistema_reservas = crear_sistema()

def obtener_reservas():
    reservas = []

    id_reserva = 0
    for sala in sistema_reservas.available_rooms():
        for reserva in sistema_reservas.get_room_bookings(sala):
            id_reserva += 1
            reservas.append((id_reserva, sala, reserva.start, reserva.end))
    return reservas

def agregar_reserva(room: str, start, end):
    booking_interval = Interval(start, end)

    sistema_reservas.book_room(room, booking_interval)

def cancelar_reserva(room: str, start, end):
    pass

def form_a_datetime(form):
    start = DateTime(int(form["start_year"]), int(form["start_month"]), int(form["start_day"]), int(form["start_hour"]), int(form["start_minute"]))
    end = DateTime(int(form["end_year"]), int(form["end_month"]), int(form["end_day"]), int(form["end_hour"]), int(form["end_minute"]))

    return start, end

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        return render_template('index.html')

    return render_template('index.html', reservas=obtener_reservas())

@app.route('/reservar', methods=['GET', 'POST'])
def reservar():
    if request.method == "POST":
        form = request.form
        start, end = form_a_datetime(form)

        agregar_reserva(form["sala"], start, end)


    return render_template("reservas.html", salas=sistema_reservas.available_rooms())

@app.route('/cancelar', methods=['GET', 'POST'])
def cancelar():
    if request.method == "POST":
        form = request.form
        booking = form.get("reserva")
        cancelar_reserva(booking[1], booking[2], booking[3])


    return render_template("cancelar.html", reservas=obtener_reservas())

if __name__ == '__main__':
    app.run(port=5000,debug=True)