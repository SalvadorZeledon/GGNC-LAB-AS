from database.database import get_connection
from ..models.entities.Edificios import Edificios

class EdificiosModel:
    @classmethod
    def get_all_edificios(cls):
        try:
            connection = get_connection()
            edificios_list = []

            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id_edificios, Nombre, Direccion, NumeroDePisos, CapacidadTotal
                    FROM Edificios ORDER BY Nombre ASC
                """)
                resultset = cursor.fetchall()

                for row in resultset:
                    edificio = Edificios(*row)
                    edificios_list.append(edificio.to_JSON())

            connection.close()
            return edificios_list
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_edificio_by_id(cls, id_edificios):
        try:
            connection = get_connection()
            edificio_JSON = None
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id_edificios, Nombre, Direccion, NumeroDePisos, CapacidadTotal
                    FROM Edificios WHERE id_edificios = %s
                """, (id_edificios,))
                row = cursor.fetchone()
                if row:
                    edificio = Edificios(*row)
                    edificio_JSON = edificio.to_JSON()
            connection.close()
            return edificio_JSON
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_edificio(cls, edificio: Edificios):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO Edificios(id_edificios, Nombre, Direccion, NumeroDePisos, CapacidadTotal)
                    VALUES (%s, %s, %s, %s, %s)
                """, (
                    edificio.id_edificios,
                    edificio.Nombre,
                    edificio.Direccion,
                    edificio.NumeroDePisos,
                    edificio.CapacidadTotal
                ))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_edificio(cls, edificio: Edificios):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE Edificios SET Nombre = %s, Direccion = %s,
                    NumeroDePisos = %s, CapacidadTotal = %s WHERE id_edificios = %s
                """, (
                    edificio.Nombre, edificio.Direccion,
                    edificio.NumeroDePisos, edificio.CapacidadTotal,
                    edificio.id_edificios
                ))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_edificio(cls, edificio: Edificios):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM Edificios WHERE id_edificios = %s", (edificio.id_edificios,))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
