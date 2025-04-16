from database.database import get_connection
from .entities.Telefonos import Telefono

class TelefonoModel:
    @classmethod
    def get_all_telefonos(cls):
        try:
            connection = get_connection()
            telefonos = []
            with connection.cursor() as cursor:
                cursor.execute("SELECT id_telefono, nombre, numero_telefono, fecha_creacion FROM telefonos ORDER BY fecha_creacion DESC")
                rows = cursor.fetchall()
                for row in rows:
                    telefono = Telefono(row[0], row[1], row[2], row[3])
                    telefonos.append(telefono.to_JSON())
            connection.close()
            return telefonos
        except Exception as e:
            raise Exception(e)

    @classmethod
    def add_telefono(cls, telefono: Telefono):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO telefonos (id_telefono, nombre, numero_telefono, fecha_creacion) VALUES (%s, %s, %s, %s)",
                               (telefono.id_telefono, telefono.nombre, telefono.numero_telefono, telefono.fecha_creacion))
                connection.commit()
            connection.close()
            return 1
        except Exception as e:
            raise Exception(e)

    @classmethod
    def delete_telefono(cls, telefono: Telefono):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM telefonos WHERE id_telefono = %s", (telefono.id_telefono,))
                connection.commit()
                affected_rows = cursor.rowcount
            connection.close()
            return affected_rows
        except Exception as e:
            raise Exception(e)
