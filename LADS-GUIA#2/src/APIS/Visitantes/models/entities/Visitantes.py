from utils.DateFormat import DateFormat

class Visitantes:
    def __init__(self, id_visitantes, Nombre, Apellido, DUI, FechaVisita, id_estudiantes):
        self.id_visitantes = id_visitantes
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.DUI = DUI
        self.FechaVisita = DateFormat.convert_date(FechaVisita)
        self.id_estudiantes = id_estudiantes

    def to_JSON(self):
        return {
            "id_visitantes": self.id_visitantes,
            "Nombre": self.Nombre,
            "Apellido": self.Apellido,
            "DUI": self.DUI,
            "FechaVisita": self.FechaVisita,
            "id_estudiantes": self.id_estudiantes
        }
