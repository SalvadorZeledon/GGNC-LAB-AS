from database.database import get_connection
from ..models.entities.Contratos import Contratos

class ContratoModel:
    @classmethod
    def get_all_contratos(cls):
        try:
            connection = get_connection()
            contratos_list = []

            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id_Contratos, FechaInicio, FechaFin, MontoMensual, Estado, id_estudiantes, id_habitaciones
                    FROM Contratos
                    ORDER BY FechaInicio ASC
                """)
                resultset = cursor.fetchall()

                for row in resultset:
                    contrato = Contratos(
                        id_contratos = row[0],
                        FechaInicio = row[1],
                        FechaFin = row[2],
                        MontoMensual = row[3],
                        Estado = row[4],
                        id_estudiantes = row[5],
                        id_habitaciones = row[6]
                    )
                    contratos_list.append(contrato.to_JSON())

            connection.close()
            return contratos_list

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_contrato_by_id(cls, id_contratos):
        try:
            connection = get_connection()
            contrato_JSON = None
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id_Contratos, FechaInicio, FechaFin, MontoMensual, Estado, id_estudiantes, id_habitaciones 
                    FROM Contratos 
                    WHERE id_Contratos = %s
                """, (id_contratos,))
                row = cursor.fetchone()
                if row is not None:
                    contrato = Contratos(
                        id_contratos = row[0],
                        FechaInicio = row[1],
                        FechaFin = row[2],
                        MontoMensual = row[3],
                        Estado = row[4],
                        id_estudiantes = row[5],
                        id_habitaciones = row[6]
                    )
                    contrato_JSON = contrato.to_JSON()
            connection.close()
            return contrato_JSON
        except Exception as ex:
            raise Exception(ex)

    
    @classmethod
    def add_contrato(cls, contrato: Contratos):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO Contratos (
                        id_contratos, FechaInicio, FechaFin, 
                        MontoMensual, Estado, id_estudiantes, id_habitaciones
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (
                    contrato.id_contratos,
                    contrato.FechaInicio,
                    contrato.FechaFin,
                    contrato.MontoMensual,
                    contrato.Estado,
                    contrato.id_estudiantes,
                    contrato.id_habitaciones
                ))

                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows

        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def update_contrato(cls, contrato: Contratos):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""update Contratos set FechaInicio = %s, FechaFin= %s, MontoMensual= %s, Estado = %s, id_estudiantes = %s, id_habitaciones = %s where id_Contratos = %s """, 
                               (contrato.FechaInicio, contrato.FechaFin, contrato.MontoMensual, contrato.Estado, contrato.id_estudiantes, contrato.id_habitaciones, contrato.id_contratos))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def delete_contratos(cls, contrato: Contratos):
        try:
            connection =  get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM Contratos WHERE id_Contratos = %s", (contrato.id_contratos,))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)