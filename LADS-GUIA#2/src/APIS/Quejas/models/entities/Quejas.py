from utils.DateFormat import DateFormat

class Quejas:
    def __init__(self, id_quejas, Fecha, Descripcion, Estado, id_estudiantes):
        self.id_quejas = id_quejas
        self.Fecha = DateFormat.convert_date(Fecha)
        self.Descripcion = Descripcion
        self.Estado = Estado
        self.id_estudiantes = id_estudiantes

    def to_JSON(self):
        return {
            "id_quejas": self.id_quejas,
            "Fecha": self.Fecha,
            "Descripcion": self.Descripcion,
            "Estado": self.Estado,
            "id_estudiantes": self.id_estudiantes
        }
