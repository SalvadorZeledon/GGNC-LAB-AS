from utils.DateFormat import DateFormat

class Contratos:
    def __init__(self, id_contratos, FechaInicio, FechaFin, MontoMensual, Estado, id_estudiantes, id_habitaciones):
        self.id_contratos = id_contratos
        self.FechaInicio = DateFormat.convert_date(FechaInicio)
        self.FechaFin =  DateFormat.convert_date(FechaFin)
        self.MontoMensual = MontoMensual
        self.Estado = Estado
        self.id_estudiantes = id_estudiantes
        self.id_habitaciones = id_habitaciones
        
    def to_JSON(self):
        return{
            "id_contratos": self.id_contratos,
            "Fecha Inicio": self.FechaInicio,
            "Fecha de Finalizacion": self.FechaFin,
            "Monto Mensual": self.MontoMensual,
            "Estado ": self.Estado,
            "ID_Estudiante": self.id_estudiantes,
            "ID_Habitacion": self.id_habitaciones

        }