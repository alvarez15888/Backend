from app.database import get_db
from app.models import Reservation
from app.schemas import ReservationCreate
import mysql.connector

def create_reservation(reservation: ReservationCreate):
    connection = get_db()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO reservations (name, email, phone, date_time, number_of_people)
        VALUES (%s, %s, %s, %s, %s)
    """, (reservation.name, reservation.email, reservation.phone, reservation.date_time, reservation.number_of_people))
    connection.commit()
    reservation_id = cursor.lastrowid
    cursor.close()
    connection.close()
    return Reservation(id=reservation_id, **reservation.dict())

def get_reservations(skip: int = 0, limit: int = 10):
    connection = get_db()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM reservations LIMIT %s OFFSET %s", (limit, skip))
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return [Reservation(**row) for row in rows]

def get_reservation(reservation_id: int):
    connection = get_db()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM reservations WHERE id = %s", (reservation_id,))
    row = cursor.fetchone()
    cursor.close()
    connection.close()
    if row:
        return Reservation(**row)
    return None

def update_reservation(reservation_id: int, reservation: ReservationCreate):
    connection = get_db()
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE reservations
        SET name = %s, email = %s, phone = %s, date_time = %s, number_of_people = %s
        WHERE id = %s
    """, (reservation.name, reservation.email, reservation.phone, reservation.date_time, reservation.number_of_people, reservation_id))
    connection.commit()
    cursor.close()
    connection.close()
    return get_reservation(reservation_id)

def delete_reservation(reservation_id: int):
    connection = get_db()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM reservations WHERE id = %s", (reservation_id,))
    connection.commit()
    cursor.close()
    connection.close()
    return True
