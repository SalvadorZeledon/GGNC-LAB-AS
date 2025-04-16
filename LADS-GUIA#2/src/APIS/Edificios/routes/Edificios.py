from flask import Blueprint, request, jsonify
import uuid
from ..models.EdificiosModel import EdificiosModel
from ..models.entities.Edificios import Edificios

main = Blueprint('edificios_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_edificios():
    try:
        edificios = EdificiosModel.get_all_edificios()
        return jsonify(edificios), 200
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500

@main.route('/<uuid:id>', methods=['GET'])
def get_edificio(id):
    try:
        edificio = EdificiosModel.get_edificio_by_id(str(id))
        if edificio:
            return jsonify(edificio), 200
        else:
            return jsonify({'message': 'Edificio no encontrado'}), 404
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_edificio():
    try:
        data = request.get_json()
        required = ['Nombre', 'Direccion', 'NumeroDePisos', 'CapacidadTotal']
        if not all(field in data for field in required):
            return jsonify({'error': 'Faltan campos requeridos'}), 400

        id_edificios = str(uuid.uuid4())
        edificio = Edificios(
            id_edificios,
            data['Nombre'],
            data['Direccion'],
            data['NumeroDePisos'],
            data['CapacidadTotal']
        )
        EdificiosModel.add_edificio(edificio)
        return jsonify({'message': 'Edificio agregado', 'id': id_edificios}), 201
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500

@main.route('update/<uuid:id>', methods=['PUT'])
def update_edificio(id):
    try:
        data = request.get_json()
        edificio = Edificios(
            str(id),
            data.get('Nombre'),
            data.get('Direccion'),
            data.get('NumeroDePisos'),
            data.get('CapacidadTotal')
        )
        affected = EdificiosModel.update_edificio(edificio)
        if affected == 1:
            return jsonify({'message': 'Edificio actualizado correctamente'}), 200
        else:
            return jsonify({'error': 'No se pudo actualizar'}), 400
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500

@main.route('delete/<uuid:id>', methods=['DELETE'])
def delete_edificio(id):
    try:
        edificio = Edificios(id_edificios=str(id), Nombre="", Direccion="", NumeroDePisos=0, CapacidadTotal=0)
        affected = EdificiosModel.delete_edificio(edificio)
        if affected == 1:
            return jsonify({'message': f'Edificio {id} eliminado'}), 200
        else:
            return jsonify({'error': 'No se encontró el edificio'}), 404
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500
