class Evento():
    def __init__(self, id_evento=None, nombre_evento=None, descripcion=None, fecha=None, hora=None, latitud=None, longitud=None) -> None:
        self.id_evento = id_evento
        self.nombre_evento = nombre_evento
        self.descripcion = descripcion
        self.fecha = fecha
        self.hora = hora
        self.latitud = latitud
        self.longitud = longitud
        
    def to_JSON(self):
        return{
            'id_evento': self.id_evento,
            'nombre_evento': self.nombre_evento,
            'descripcion': self.descripcion,
            'fecha': self.fecha,
            'hora': self.hora,
            'latitud': self.latitud,
            'longitud': self.longitud
        }