from database.database import get_connection
from ..models.entities.Visitantes import Visitantes

class VisitantesModel:
    @classmethod
    def get_all_visitantes(cls):
        try:
            connection = get_connection()
            visitantes_list = []
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id_visitantes, Nombre, Apellido, DUI, FechaVisita, id_estudiantes
                    FROM Visitantes ORDER BY FechaVisita DESC
                """)
                resultset = cursor.fetchall()
                for row in resultset:
                    visitante = Visitantes(*row)
                    visitantes_list.append(visitante.to_JSON())
            connection.close()
            return visitantes_list
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_visitante_by_id(cls, id_visitantes):
        try:
            connection = get_connection()
            visitante_JSON = None
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id_visitantes, Nombre, Apellido, DUI, FechaVisita, id_estudiantes
                    FROM Visitantes WHERE id_visitantes = %s
                """, (id_visitantes,))
                row = cursor.fetchone()
                if row:
                    visitante = Visitantes(*row)
                    visitante_JSON = visitante.to_JSON()
            connection.close()
            return visitante_JSON
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_visitante(cls, visitante: Visitantes):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO Visitantes(id_visitantes, Nombre, Apellido, DUI, FechaVisita, id_estudiantes)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (
                    visitante.id_visitantes,
                    visitante.Nombre,
                    visitante.Apellido,
                    visitante.DUI,
                    visitante.FechaVisita,
                    visitante.id_estudiantes
                ))
                connection.commit()
                return cursor.rowcount
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def update_visitante(cls, visitante: Visitantes):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE visitantes SET
                        nombre = %s,
                        apellido = %s,
                        dui = %s,
                        fechavisita = %s,
                        id_estudiantes = %s
                    WHERE id_visitantes = %s
                """, (
                    visitante.Nombre,
                    visitante.Apellido,
                    visitante.DUI,
                    visitante.FechaVisita,
                    visitante.id_estudiantes,
                    visitante.id_visitantes
                ))
                connection.commit()
                return cursor.rowcount
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def delete_visitante(cls, visitante: Visitantes):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM Visitantes WHERE id_visitantes = %s", (visitante.id_visitantes,))
                connection.commit()
                return cursor.rowcount
        except Exception as ex:
            raise Exception(ex)
