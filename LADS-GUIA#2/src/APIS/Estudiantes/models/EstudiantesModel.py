from database.database import get_connection
from ..models.entities.Estudiantes import Estudiantes

class EstudiantesModel:
    @classmethod
    def get_all_estudiantes(cls):
        try:
            connection = get_connection()
            estudiantes_list = []
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id_estudiantes, Nombre, Apellido, Carnet, FechaNacimiento, Genero, Carrera, Telefono, Email
                    FROM Estudiantes ORDER BY Apellido ASC
                """)
                resultset = cursor.fetchall()
                for row in resultset:
                    estudiante = Estudiantes(*row)
                    estudiantes_list.append(estudiante.to_JSON())
            connection.close()
            return estudiantes_list
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_estudiante_by_id(cls, id_estudiantes):
        try:
            connection = get_connection()
            estudiante_JSON = None
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id_estudiantes, Nombre, Apellido, Carnet, FechaNacimiento, Genero, Carrera, Telefono, Email
                    FROM Estudiantes WHERE id_estudiantes = %s
                """, (id_estudiantes,))
                row = cursor.fetchone()
                if row:
                    estudiante = Estudiantes(*row)
                    estudiante_JSON = estudiante.to_JSON()
            connection.close()
            return estudiante_JSON
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_estudiante(cls, estudiante: Estudiantes):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO Estudiantes(id_estudiantes, Nombre, Apellido, Carnet, FechaNacimiento, Genero, Carrera, Telefono, Email)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (
                    estudiante.id_estudiantes,
                    estudiante.Nombre,
                    estudiante.Apellido,
                    estudiante.Carnet,
                    estudiante.FechaNacimiento,
                    estudiante.Genero,
                    estudiante.Carrera,
                    estudiante.Telefono,
                    estudiante.Email
                ))
                connection.commit()
                return cursor.rowcount
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_estudiante(cls, estudiante: Estudiantes):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE Estudiantes
                    SET Nombre = %s, Apellido = %s, Carnet = %s, FechaNacimiento = %s,
                        Genero = %s, Carrera = %s, Telefono = %s, Email = %s
                    WHERE id_estudiantes = %s
                """, (
                    estudiante.Nombre,
                    estudiante.Apellido,
                    estudiante.Carnet,
                    estudiante.FechaNacimiento,
                    estudiante.Genero,
                    estudiante.Carrera,
                    estudiante.Telefono,
                    estudiante.Email,
                    estudiante.id_estudiantes
                ))
                connection.commit()
                return cursor.rowcount
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_estudiante(cls, estudiante: Estudiantes):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM Estudiantes WHERE id_estudiantes = %s", (estudiante.id_estudiantes,))
                connection.commit()
                return cursor.rowcount
        except Exception as ex:
            raise Exception(ex)
