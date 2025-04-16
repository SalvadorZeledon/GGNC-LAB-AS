from utils.DateFormat import DateFormat

class Estudiantes:
    def __init__(self, id_estudiantes, Nombre, Apellido, Carnet, FechaNacimiento, Genero, Carrera, Telefono, Email):
        self.id_estudiantes = id_estudiantes
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Carnet = Carnet
        self.FechaNacimiento = DateFormat.convert_date(FechaNacimiento)
        self.Genero = Genero
        self.Carrera = Carrera
        self.Telefono = Telefono
        self.Email = Email

    def to_JSON(self):
        return {
            "id_estudiantes": self.id_estudiantes,
            "Nombre": self.Nombre,
            "Apellido": self.Apellido,
            "Carnet": self.Carnet,
            "FechaNacimiento": self.FechaNacimiento,
            "Genero": self.Genero,
            "Carrera": self.Carrera,
            "Telefono": self.Telefono,
            "Email": self.Email
        }

