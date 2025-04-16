from database.database import get_connection
from ..models.entities.Mantenimiento import Mantenimiento

class MantenimientoModel:
    @classmethod
    def get_all_mantenimientos(cls):
        try:
            connection = get_connection()
            mantenimiento_list = []
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id_mantenimiento, FechaSolicitud, DescripcionProblema, FechaResolucion, Estado, id_habitaciones
                    FROM Mantenimiento ORDER BY FechaSolicitud DESC
                """)
                resultset = cursor.fetchall()
                for row in resultset:
                    mantenimiento = Mantenimiento(*row)
                    mantenimiento_list.append(mantenimiento.to_JSON())
            connection.close()
            return mantenimiento_list
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_mantenimiento_by_id(cls, id_mantenimiento):
        try:
            connection = get_connection()
            mantenimiento_JSON = None
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id_mantenimiento, FechaSolicitud, DescripcionProblema, FechaResolucion, Estado, id_habitaciones
                    FROM Mantenimiento WHERE id_mantenimiento = %s
                """, (id_mantenimiento,))
                row = cursor.fetchone()
                if row:
                    mantenimiento = Mantenimiento(*row)
                    mantenimiento_JSON = mantenimiento.to_JSON()
            connection.close()
            return mantenimiento_JSON
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_mantenimiento(cls, mantenimiento: Mantenimiento):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO Mantenimiento (id_mantenimiento, FechaSolicitud, DescripcionProblema, FechaResolucion, Estado, id_habitaciones)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (
                    mantenimiento.id_mantenimiento,
                    mantenimiento.FechaSolicitud,
                    mantenimiento.DescripcionProblema,
                    mantenimiento.FechaResolucion,
                    mantenimiento.Estado,
                    mantenimiento.id_habitaciones
                ))
                connection.commit()
                return cursor.rowcount
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_mantenimiento(cls, mantenimiento: Mantenimiento):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE Mantenimiento SET
                        FechaSolicitud = %s,
                        DescripcionProblema = %s,
                        FechaResolucion = %s,
                        Estado = %s,
                        id_habitaciones = %s
                    WHERE id_mantenimiento = %s
                """, (
                    mantenimiento.FechaSolicitud,
                    mantenimiento.DescripcionProblema,
                    mantenimiento.FechaResolucion,
                    mantenimiento.Estado,
                    mantenimiento.id_habitaciones,
                    mantenimiento.id_mantenimiento
                ))
                connection.commit()
                return cursor.rowcount
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_mantenimiento(cls, mantenimiento: Mantenimiento):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM Mantenimiento WHERE id_mantenimiento = %s", (mantenimiento.id_mantenimiento,))
                connection.commit()
                return cursor.rowcount
        except Exception as ex:
            raise Exception(ex)
