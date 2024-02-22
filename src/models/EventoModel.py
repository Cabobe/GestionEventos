from database.db import get_connection
from entities.Evento import Evento
    
class EventoModel():

    #Listar todos los eventos
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
                eventos.append(evento.to_JSON())
                       
            connection.close()
            return eventos

        except Exception as ex:
            raise Exception(ex) 

    #Listar un solo evento
    @classmethod
    def get_evento(self,id_evento):
        try:
            connection=get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""SELECT id_evento, nombre_evento, descripcion, fecha_inicio, hora_inicio, fecha_fin, hora_fin, latitud, longitud FROM "GestionEventos"."Eventos" WHERE id_evento = %s""",(id_evento))
                row=cursor.fetchone()

                evento = None
                if row != None:
                    evento = Evento(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
                    evento = evento.to_JSON()
                       
            connection.close()
            return evento

        except Exception as ex:
            raise Exception(ex) 
    
    #Insertar un evento
   
  
    #Actualizar un evento
        
    
    #Borrar un evento