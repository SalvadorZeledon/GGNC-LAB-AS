from database.database import get_connection
from ..models.entities.Habitaciones import Habitaciones

class HabitacionesModel:
    @classmethod
    def get_all_habitaciones(cls):
        try:
            connection = get_connection()
            habitaciones_list = []
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id_habitaciones, Numero, Piso, Tipo, Capacidad, Estado, id_edificios
                    FROM Habitaciones ORDER BY Numero
                """)
                resultset = cursor.fetchall()
                for row in resultset:
                    habitacion = Habitaciones(*row)
                    habitaciones_list.append(habitacion.to_JSON())
            connection.close()
            return habitaciones_list
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_habitacion_by_id(cls, id_habitaciones):
        try:
            connection = get_connection()
            habitacion_JSON = None
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id_habitaciones, Numero, Piso, Tipo, Capacidad, Estado, id_edificios
                    FROM Habitaciones WHERE id_habitaciones = %s
                """, (id_habitaciones,))
                row = cursor.fetchone()
                if row:
                    habitacion = Habitaciones(*row)
                    habitacion_JSON = habitacion.to_JSON()
            connection.close()
            return habitacion_JSON
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_habitacion(cls, habitacion: Habitaciones):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO Habitaciones(id_habitaciones, Numero, Piso, Tipo, Capacidad, Estado, id_edificios)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (
                    habitacion.id_habitaciones,
                    habitacion.Numero,
                    habitacion.Piso,
                    habitacion.Tipo,
                    habitacion.Capacidad,
                    habitacion.Estado,
                    habitacion.id_edificios
                ))
                connection.commit()
                return cursor.rowcount
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_habitacion(cls, habitacion: Habitaciones):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE Habitaciones SET
                    Numero = %s, Piso = %s, Tipo = %s, Capacidad = %s, Estado = %s, id_edificios = %s
                    WHERE id_habitaciones = %s
                """, (
                    habitacion.Numero,
                    habitacion.Piso,
                    habitacion.Tipo,
                    habitacion.Capacidad,
                    habitacion.Estado,
                    habitacion.id_edificios,
                    habitacion.id_habitaciones
                ))
                connection.commit()
                return cursor.rowcount
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_habitacion(cls, habitacion: Habitaciones):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM Habitaciones WHERE id_habitaciones = %s", (habitacion.id_habitaciones,))
                connection.commit()
                return cursor.rowcount
        except Exception as ex:
            raise Exception(ex)
