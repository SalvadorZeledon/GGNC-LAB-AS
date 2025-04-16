from utils.DateFormat import DateFormat

class Mantenimiento:
    def __init__(self, id_mantenimiento, FechaSolicitud, DescripcionProblema, FechaResolucion, Estado, id_habitaciones):
        self.id_mantenimiento = id_mantenimiento
        self.FechaSolicitud = DateFormat.convert_date(FechaSolicitud)
        self.DescripcionProblema = DescripcionProblema
        self.FechaResolucion = DateFormat.convert_date(FechaResolucion) if FechaResolucion else None
        self.Estado = Estado
        self.id_habitaciones = id_habitaciones

    def to_JSON(self):
        return {
            "id_mantenimiento": self.id_mantenimiento,
            "FechaSolicitud": self.FechaSolicitud,
            "DescripcionProblema": self.DescripcionProblema,
            "FechaResolucion": self.FechaResolucion,
            "Estado": self.Estado,
            "id_habitaciones": self.id_habitaciones
        }
