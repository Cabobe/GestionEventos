from flask import Blueprint, jsonify, request
from entities.Evento import Evento 
from models.EventoModel import EventoModel 

main = Blueprint('gestioneventos_blueprint',__name__)

#Listar todos los eventos
@main.route('/')
def get_eventos():
    try:
        eventos = EventoModel.get_eventos()
        return jsonify(eventos)
    except Exception as ex:
        return jsonify({'mensaje': str(ex)}),500

#Listar un solo evento  
@main.route('/<id>')
def get_evento(id):
    try:
        evento = EventoModel.get_evento(id)
        if evento != None:
            return jsonify(evento)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'mensaje': str(ex)}), 500

#Insertar un evento
@main.route('/addEvento', methods=['POST'])
def add_evento():
    try:
        nombre_evento = request.json['nombre_evento']
        descripcion = request.json['descripcion']
        fecha = request.json['fecha']
        hora = request.json['hora']
        latitud = request.json['latitud']
        longitud = request.json['longitud']

        evento = Evento(None, nombre_evento, descripcion, fecha, hora, latitud, longitud)
        lastid = EventoModel.add_evento(evento)
        
        if lastid != "0":      
            return jsonify(lastid)
        else:
            return jsonify({'message':"Error en el insert"}) , 500
    
    except Exception as ex:
        return jsonify({'mensaje': str(ex)}), 500



#Actualizar un evento
#Borrar un evento
    