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
                cursor.execute("""SELECT id_evento, nombre_evento, descripcion, fecha, hora, latitud, longitud FROM "GestionEventos"."Eventos" ORDER BY 1""")
                resultset=cursor.fetchall()

            for row in resultset:
                evento=Evento(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
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
                cursor.execute("""SELECT id_evento, nombre_evento, descripcion, fecha, hora, latitud, longitud 
                                  FROM "GestionEventos"."Eventos" 
                                  WHERE id_evento = %s""",(id_evento,))
                row=cursor.fetchone()

                evento = None
                if row != None:
                    evento = Evento(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
                    evento = evento.to_JSON()
                       
            connection.close()
            return evento

        except Exception as ex:
            raise Exception(ex) 
    
    #Insertar un evento
    @classmethod
    def add_evento(self,evento):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO "GestionEventos"."Eventos"(nombre_evento, descripcion, fecha, hora, latitud, longitud) 
                                  VALUES (%s,%s,%s,%s,%s,%s)""", 
                                  (evento.nombre_evento, evento.descripcion, evento.fecha, evento.hora, evento.latitud, evento.longitud))
                connection.commit()
                
                cursor.execute('SELECT LASTVAL()')
                row=cursor.fetchone()
                if row != None:
                    lastid = str(row[0])
                else:
                    lastid = "0"
                connection.close()
                return lastid

        except Exception as ex:
            raise Exception(ex) 
        
    #Actualizar un evento
    @classmethod
    def update_evento(self,evento):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE "GestionEventos"."Eventos"
                                    SET 
                                    nombre_evento=%s, 
                                    descripcion=%s, 
                                    fecha=%s,
                                    hora=%s, 
                                    latitud=%s, 
                                    longitud=%s
                                    WHERE id_evento=%s""", 
                                  (evento.nombre_evento, evento.descripcion, evento.fecha, evento.hora, evento.latitud, evento.longitud, evento.id_evento))
                rowaffected = cursor.rowcount
                connection.commit()
                connection.close()
                return str(rowaffected)

        except Exception as ex:
            raise Exception(ex)    
    
    #Borrar un evento
    @classmethod
    def delete_evento(self,id_evento):
        try:
            connection=get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""DELETE FROM "GestionEventos"."Eventos" 
                                  WHERE id_evento = %s""",(id_evento,))
                rowaffected = cursor.rowcount
                connection.commit()
                connection.close()
                return str(rowaffected)

        except Exception as ex:
            raise Exception(ex) 