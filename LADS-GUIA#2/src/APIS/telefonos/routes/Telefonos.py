from flask import Blueprint, request, jsonify
import uuid
from ..models.TelefonosModel import TelefonoModel
from ..models.entities.Telefonos import Telefono
from datetime import datetime

main = Blueprint('telefonos_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_telefonos():
    try:
        telefonos = TelefonoModel.get_all_telefonos()
        return jsonify(telefonos), 200
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_telefono():
    try:
        data = request.get_json()
        if 'nombre' not in data or 'numero_telefono' not in data:
            return jsonify({'error': 'Campos requeridos: nombre, numero_telefono'}), 400

        telefono = Telefono(
            id_telefono=str(uuid.uuid4()),
            nombre=data['nombre'],
            numero_telefono=data['numero_telefono']
        )
        TelefonoModel.add_telefono(telefono)
        return jsonify({'message': 'Telefono agregado exitosamente'}), 201
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500

@main.route('/delete/<uuid:id>', methods=['DELETE'])
def delete_telefono(id):
    try:
        telefono = Telefono(id_telefono=str(id), nombre='', numero_telefono='')
        affected = TelefonoModel.delete_telefono(telefono)
        if affected == 1:
            return jsonify({'message': f'Telefono {id} eliminado'}), 200
        else:
            return jsonify({'error': 'Telefono no encontrado'}), 404
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500