from utils.DateFormat import DateFormat

class Notificaciones:
    def __init__(self, id_notificaciones, id_estudiantes, fecha_envio, estado, mensaje):
        self.id_notificaciones = id_notificaciones
        self.id_estudiantes = id_estudiantes
        self.fecha_envio = DateFormat.convert_date(fecha_envio)
        self.estado = estado
        self.mensaje = mensaje

    def to_JSON(self):
        return {
            "id_notificaciones": self.id_notificaciones,
            "id_estudiantes": self.id_estudiantes,
            "fecha_envio": self.fecha_envio,
            "estado": self.estado,
            "mensaje": self.mensaje
        }
