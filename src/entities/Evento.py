from utils.DateFormat import DateFormat

class Evento():
    def __init__(self, id_evento, nombre_evento=None, descripcion=None, fecha_inicio=None, hora_inicio=None, fecha_fin=None, hora_fin=None, latitud=None, longitud=None) -> None:
        self.id_evento = id_evento
        self.nombre_evento = nombre_evento
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.hora_inicio = hora_inicio
        self.fecha_fin = fecha_fin
        self.hora_fin = hora_fin
        self.latitud = latitud
        self.longitud = longitud
        
    def to_JSON(self):
        return{
            'id_evento': self.id_evento,
            'nombre_evento': self.nombre_evento,
            'descripcion': self.descripcion,
            'fecha_inicio': DateFormat.convert_date(self.fecha_inicio),
            'hora_inicio': self.hora_inicio,
            'fecha_fin': DateFormat.convert_date(self.fecha_fin),
            'hora_fin': self.hora_fin,
            'latitud': self.latitud,
            'longitud': self.longitud
        }