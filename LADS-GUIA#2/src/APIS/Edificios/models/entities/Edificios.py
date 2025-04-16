class Edificios:
    def __init__(self, id_edificios, Nombre, Direccion, NumeroDePisos, CapacidadTotal):
        self.id_edificios = id_edificios
        self.Nombre = Nombre
        self.Direccion = Direccion
        self.NumeroDePisos = NumeroDePisos
        self.CapacidadTotal = CapacidadTotal

    def to_JSON(self):
        return {
            "id_edificios": self.id_edificios,
            "Nombre": self.Nombre,
            "Direccion": self.Direccion,
            "NumeroDePisos": self.NumeroDePisos,
            "CapacidadTotal": self.CapacidadTotal
        }
