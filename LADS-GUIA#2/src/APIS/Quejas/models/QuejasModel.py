from database.database import get_connection
from ..models.entities.Quejas import Quejas

class QuejasModel:
    @classmethod
    def get_all_quejas(cls):
        try:
            connection = get_connection()
            quejas_list = []
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id_quejas, Fecha, Descripcion, Estado, id_estudiantes
                    FROM Quejas ORDER BY Fecha DESC
                """)
                resultset = cursor.fetchall()
                for row in resultset:
                    queja = Quejas(*row)
                    quejas_list.append(queja.to_JSON())
            connection.close()
            return quejas_list
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_queja_by_id(cls, id_quejas):
        try:
            connection = get_connection()
            queja_JSON = None
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id_quejas, Fecha, Descripcion, Estado, id_estudiantes
                    FROM Quejas WHERE id_quejas = %s
                """, (id_quejas,))
                row = cursor.fetchone()
                if row:
                    queja = Quejas(*row)
                    queja_JSON = queja.to_JSON()
            connection.close()
            return queja_JSON
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_queja(cls, queja: Quejas):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO Quejas(id_quejas, Fecha, Descripcion, Estado, id_estudiantes)
                    VALUES (%s, %s, %s, %s, %s)
                """, (
                    queja.id_quejas,
                    queja.Fecha,
                    queja.Descripcion,
                    queja.Estado,
                    queja.id_estudiantes
                ))
                connection.commit()
                return cursor.rowcount
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_queja(cls, queja: Quejas):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE Quejas SET Fecha=%s, Descripcion=%s, Estado=%s, id_estudiantes=%s
                    WHERE id_quejas = %s
                """, (
                    queja.Fecha,
                    queja.Descripcion,
                    queja.Estado,
                    queja.id_estudiantes,
                    queja.id_quejas
                ))
                connection.commit()
                return cursor.rowcount
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_queja(cls, queja: Quejas):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM Quejas WHERE id_quejas = %s", (queja.id_quejas,))
                connection.commit()
                return cursor.rowcount
        except Exception as ex:
            raise Exception(ex)
