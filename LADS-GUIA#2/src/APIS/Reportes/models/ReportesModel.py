from database.database import get_connection
from ..models.entities.Reportes import Reportes

class ReportesModel:
    @classmethod
    def get_all_reportes(cls):
        try:
            connection = get_connection()
            reportes_list = []
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id_reportes, TipoReporte, FechaGeneracion, Descripcion, RutaArchivo
                    FROM Reportes ORDER BY FechaGeneracion DESC
                """)
                resultset = cursor.fetchall()
                for row in resultset:
                    reporte = Reportes(*row)
                    reportes_list.append(reporte.to_JSON())
            connection.close()
            return reportes_list
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_reporte_by_id(cls, id_reportes):
        try:
            connection = get_connection()
            reporte_JSON = None
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id_reportes, TipoReporte, FechaGeneracion, Descripcion, RutaArchivo
                    FROM Reportes WHERE id_reportes = %s
                """, (id_reportes,))
                row = cursor.fetchone()
                if row:
                    reporte = Reportes(*row)
                    reporte_JSON = reporte.to_JSON()
            connection.close()
            return reporte_JSON
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_reporte(cls, reporte: Reportes):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO Reportes(id_reportes, TipoReporte, FechaGeneracion, Descripcion, RutaArchivo)
                    VALUES (%s, %s, %s, %s, %s)
                """, (
                    reporte.id_reportes,
                    reporte.TipoReporte,
                    reporte.FechaGeneracion,
                    reporte.Descripcion,
                    reporte.RutaArchivo
                ))
                connection.commit()
                return cursor.rowcount
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def update_reporte(cls, reporte: Reportes):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE reportes SET
                        tiporeporte = %s,
                        fechageneracion = %s,
                        descripcion = %s,
                        rutaarchivo = %s
                    WHERE id_reportes = %s
                """, (
                    reporte.TipoReporte,
                    reporte.FechaGeneracion,
                    reporte.Descripcion,
                    reporte.RutaArchivo,
                    reporte.id_reportes
                ))
                connection.commit()
                return cursor.rowcount
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_reporte(cls, reporte: Reportes):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM Reportes WHERE id_reportes = %s", (reporte.id_reportes,))
                connection.commit()
                return cursor.rowcount
        except Exception as ex:
            raise Exception(ex)
