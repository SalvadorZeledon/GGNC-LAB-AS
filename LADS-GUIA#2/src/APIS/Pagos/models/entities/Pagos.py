from utils.DateFormat import DateFormat

class Pagos:
    def __init__(self, id_pagos, FechaPago, Monto, MetodoPago, EstadoPago, id_contratos):
        self.id_pagos = id_pagos
        self.FechaPago = DateFormat.convert_date(FechaPago)
        self.Monto = Monto
        self.MetodoPago = MetodoPago
        self.EstadoPago = EstadoPago
        self.id_contratos = id_contratos

    def to_JSON(self):
        return {
            "id_pagos": self.id_pagos,
            "FechaPago": self.FechaPago,
            "Monto": self.Monto,
            "MetodoPago": self.MetodoPago,
            "EstadoPago": self.EstadoPago,
            "id_contratos": self.id_contratos
        }
