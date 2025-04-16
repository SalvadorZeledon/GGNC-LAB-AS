from database.database import get_connection
from ..models.entities.Pagos import Pagos

class PagosModel:
    @classmethod
    def get_all_pagos(cls):
        try:
            connection = get_connection()
            pagos_list = []
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id_pagos, FechaPago, Monto, MetodoPago, EstadoPago, id_contratos
                    FROM Pagos ORDER BY FechaPago DESC
                """)
                resultset = cursor.fetchall()
                for row in resultset:
                    pago = Pagos(*row)
                    pagos_list.append(pago.to_JSON())
            connection.close()
            return pagos_list
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_pago_by_id(cls, id_pagos):
        try:
            connection = get_connection()
            pago_JSON = None
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id_pagos, FechaPago, Monto, MetodoPago, EstadoPago, id_contratos
                    FROM Pagos WHERE id_pagos = %s
                """, (id_pagos,))
                row = cursor.fetchone()
                if row:
                    pago = Pagos(*row)
                    pago_JSON = pago.to_JSON()
            connection.close()
            return pago_JSON
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_pago(cls, pago: Pagos):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO Pagos(id_pagos, FechaPago, Monto, MetodoPago, EstadoPago, id_contratos)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (
                    pago.id_pagos,
                    pago.FechaPago,
                    pago.Monto,
                    pago.MetodoPago,
                    pago.EstadoPago,
                    pago.id_contratos
                ))
                connection.commit()
                return cursor.rowcount
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_pago(cls, pago: Pagos):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE Pagos SET FechaPago=%s, Monto=%s, MetodoPago=%s, EstadoPago=%s, id_contratos=%s
                    WHERE id_pagos = %s
                """, (
                    pago.FechaPago,
                    pago.Monto,
                    pago.MetodoPago,
                    pago.EstadoPago,
                    pago.id_contratos,
                    pago.id_pagos
                ))
                connection.commit()
                return cursor.rowcount
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_pago(cls, pago: Pagos):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM Pagos WHERE id_pagos = %s", (pago.id_pagos,))
                connection.commit()
                return cursor.rowcount
        except Exception as ex:
            raise Exception(ex)
