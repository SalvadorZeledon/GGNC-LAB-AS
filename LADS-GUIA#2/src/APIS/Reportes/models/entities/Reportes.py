from utils.DateFormat import DateFormat

class Reportes:
    def __init__(self, id_reportes, TipoReporte, FechaGeneracion, Descripcion, RutaArchivo):
        self.id_reportes = id_reportes
        self.TipoReporte = TipoReporte
        self.FechaGeneracion = DateFormat.convert_date(FechaGeneracion)
        self.Descripcion = Descripcion
        self.RutaArchivo = RutaArchivo

    def to_JSON(self):
        return {
            "id_reportes": self.id_reportes,
            "TipoReporte": self.TipoReporte,
            "FechaGeneracion": self.FechaGeneracion,
            "Descripcion": self.Descripcion,
            "RutaArchivo": self.RutaArchivo
        }
