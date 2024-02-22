from flask import Blueprint, jsonify, request
from entities.Evento import Evento 
from models.EventoModel import EventoModel 

main = Blueprint('gestioneventos_blueprint',__name__)

@main.route('/')
def get_eventos():
    try:
        eventos = EventoModel.get_eventos()
        return jsonify(eventos)
    except Exception as ex:
        return jsonify({'mensaje': str(ex)}),500
    
@main.route('/<id>')
def get_evento(id):
    try:
        evento = EventoModel.get_evento(id)
        if evento != None:
            return jsonify(evento)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'mensaje': str(ex)}),500
    