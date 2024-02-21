from flask import Blueprint, jsonify

from models.EventoModel import EventoModel 

main = Blueprint('routes_blueprint',__name__)

@main.route('/')
def get_eventos():
    try:
        eventos = EventoModel.get_eventos()
        return jsonify(eventos)
    except Exception as ex:
        return jsonify({'mensaje': str(ex)}),500
    