from database.database import get_connection
from ..models.entities.Notificaciones import Notificaciones

class NotificacionesModel:
    @classmethod
    def get_all_notificaciones(cls):
        try:
            connection = get_connection()
            notificaciones = []
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id, id_estudiante, fecha_envio, estado, mensaje
                    FROM notificaciones
                    ORDER BY fecha_envio DESC
                """)
                resultset = cursor.fetchall()
                for row in resultset:
                    notificacion = Notificaciones(
                        id_notificaciones=row[0],
                        id_estudiantes=row[1],
                        fecha_envio=row[2],
                        estado=row[3],
                        mensaje=row[4]
                    )
                    notificaciones.append(notificacion.to_JSON())
            connection.close()
            return notificaciones
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_notificacion_by_id(cls, id):
        try:
            connection = get_connection()
            notificacion_JSON = None
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id, id_estudiante, fecha_envio, estado, mensaje
                    FROM notificaciones
                    WHERE id = %s
                """, (id,))
                row = cursor.fetchone()
                if row:
                    notificacion = Notificaciones(
                        id_notificaciones=row[0],
                        id_estudiantes=row[1],
                        fecha_envio=row[2],
                        estado=row[3],
                        mensaje=row[4]
                    )
                    notificacion_JSON = notificacion.to_JSON()
            connection.close()
            return notificacion_JSON
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_notificacion(cls, notificacion: Notificaciones):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO notificaciones (id, id_estudiante, fecha_envio, estado, mensaje)
                    VALUES (%s, %s, %s, %s, %s)
                """, (
                    notificacion.id_notificaciones,
                    notificacion.id_estudiantes,
                    notificacion.fecha_envio,
                    notificacion.estado,
                    notificacion.mensaje
                ))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_notificacion(cls, notificacion: Notificaciones):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM notificaciones WHERE id = %s
                """, (notificacion.id_notificaciones,))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_notificacion(cls, notificacion: Notificaciones):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE notificaciones
                    SET id_estudiante = %s, fecha_envio = %s, estado = %s, mensaje = %s
                    WHERE id = %s
                """, (
                    notificacion.id_estudiantes,
                    notificacion.fecha_envio,
                    notificacion.estado,
                    notificacion.mensaje,
                    notificacion.id_notificaciones
                ))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
