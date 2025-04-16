class Habitaciones:
    def __init__(self, id_habitaciones, Numero, Piso, Tipo, Capacidad, Estado, id_edificios):
        self.id_habitaciones = id_habitaciones
        self.Numero = Numero
        self.Piso = Piso
        self.Tipo = Tipo
        self.Capacidad = Capacidad
        self.Estado = Estado
        self.id_edificios = id_edificios

    def to_JSON(self):
        return {
            "id_habitaciones": self.id_habitaciones,
            "Numero": self.Numero,
            "Piso": self.Piso,
            "Tipo": self.Tipo,
            "Capacidad": self.Capacidad,
            "Estado": self.Estado,
            "id_edificios": self.id_edificios
        }
