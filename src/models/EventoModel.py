from database.db import get_connection

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
        pass

def to_JSON(self):
    return{
        'id_evento': self.id_evento,
        'nombre_evento': self.nombre_evento,
        'descripcion': self.descripcion,
        'fecha_inicio': self.fecha_inicio,
        'hora_inicio': self.hora_inicio,
        'fecha_fin': self.fecha_fin,
        'hora_fin': self.hora_fin,
        'latitud': self.latitud,
        'longitud': self.longitud
    }
    
class EventoModel():
    @classmethod
    def get_eventos(self):
        try:
            connection=get_connection()
            eventos=[]

            with connection.cursor() as cursor:
                cursor.execute("""SELECT id_evento, nombre_evento, descripcion, fecha_inicio, hora_inicio, fecha_fin, hora_fin, latitud, longitud FROM "GestionEventos"."Eventos";""")
                resultset=cursor.fetchall()

            for row in resultset:
                evento=Evento(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
                eventos.append(evento)

            connection.close()
            return eventos

        except Exception as ex:
            raise Exception(ex) 
