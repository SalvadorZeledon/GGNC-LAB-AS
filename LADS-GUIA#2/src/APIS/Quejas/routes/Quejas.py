from flask import Blueprint, request, jsonify
import uuid
from ..models.QuejasModel import QuejasModel
from ..models.entities.Quejas import Quejas
from utils.DateFormat import DateFormat
from datetime import datetime

main = Blueprint('quejas_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_quejas():
    try:
        quejas = QuejasModel.get_all_quejas()
        return jsonify(quejas), 200
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500

@main.route('/<uuid:id>', methods=['GET'])
def get_queja(id):
    try:
        queja = QuejasModel.get_queja_by_id(str(id))
        if queja:
            return jsonify(queja), 200
        else:
            return jsonify({'message': 'Queja no encontrada'}), 404
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_queja():
    try:
        data = request.get_json()
        if 'Fecha' not in data or 'id_estudiantes' not in data:
            return jsonify({'error': 'Faltan campos obligatorios'}), 400
        
        fecha =  datetime.strptime(data.get('Fecha'), '%d/%m/%Y')
        queja = Quejas(
            id_quejas=str(uuid.uuid4()),
            Fecha=fecha,
            Descripcion=data.get('Descripcion'),
            Estado=data.get('Estado'),
            id_estudiantes=data['id_estudiantes']
        )
        QuejasModel.add_queja(queja)
        return jsonify({'message': 'Queja agregada'}), 201
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500

@main.route('update/<uuid:id>', methods=['PUT'])
def update_queja(id):
    try:
        data = request.get_json()
        fecha =  datetime.strptime(data.get('Fecha'), '%d/%m/%Y')
        queja = Quejas(
            id_quejas=str(id),
            Fecha=fecha,
            Descripcion=data.get('Descripcion'),
            Estado=data.get('Estado'),
            id_estudiantes=data.get('id_estudiantes')
        )
        affected = QuejasModel.update_queja(queja)
        if affected == 1:
            return jsonify({'message': 'Queja actualizada'}), 200
        else:
            return jsonify({'error': 'No se pudo actualizar'}), 400
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500

@main.route('delete/<uuid:id>', methods=['DELETE'])
def delete_queja(id):
    try:
        queja = Quejas(
            id_quejas=str(id),
            Fecha=datetime.now(),
            Descripcion="",
            Estado="",
            id_estudiantes=""
        )
        affected = QuejasModel.delete_queja(queja)
        if affected == 1:
            return jsonify({'message': f'Queja {id} eliminada'}), 200
        else:
            return jsonify({'error': 'Queja no encontrada'}), 404
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500
