from flask import Blueprint, request, jsonify
import uuid
from ..models.MantenimientoModel import MantenimientoModel
from ..models.entities.Mantenimiento import Mantenimiento
from utils.DateFormat import DateFormat
from datetime import datetime

main = Blueprint('mantenimiento_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_mantenimientos():
    try:
        mantenimientos = MantenimientoModel.get_all_mantenimientos()
        return jsonify(mantenimientos), 200
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500

@main.route('/<uuid:id>', methods=['GET'])
def get_mantenimiento(id):
    try:
        mantenimiento = MantenimientoModel.get_mantenimiento_by_id(str(id))
        if mantenimiento:
            return jsonify(mantenimiento), 200
        else:
            return jsonify({'message': 'No encontrado'}), 404
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_mantenimiento():
    try:
        data = request.get_json()
        if 'FechaSolicitud' not in data or 'id_habitaciones' not in data:
            return jsonify({'error': 'Faltan campos obligatorios'}), 400
        
        fecha_solicitud =  datetime.strptime(data.get('FechaSolicitud'), '%d/%m/%Y')
        fecha_resolucion =  datetime.strptime(data.get('FechaResolucion'), '%d/%m/%Y')

        mantenimiento = Mantenimiento(
            id_mantenimiento=str(uuid.uuid4()),
            FechaSolicitud=fecha_solicitud,
            DescripcionProblema=data.get('DescripcionProblema'),
            FechaResolucion=fecha_resolucion,
            Estado=data.get('Estado'),
            id_habitaciones=data['id_habitaciones']
        )
        MantenimientoModel.add_mantenimiento(mantenimiento)
        return jsonify({'message': 'Mantenimiento agregado'}), 201
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500

@main.route('update/<uuid:id>', methods=['PUT'])
def update_mantenimiento(id):
    try:
        data = request.get_json()
        fecha_solicitud =  datetime.strptime(data.get('FechaSolicitud'), '%d/%m/%Y')
        fecha_resolucion =  datetime.strptime(data.get('FechaResolucion'), '%d/%m/%Y')

        mantenimiento = Mantenimiento(
            id_mantenimiento=str(id),
            FechaSolicitud=fecha_solicitud,
            DescripcionProblema=data.get('DescripcionProblema'),
            FechaResolucion=fecha_resolucion,
            Estado=data.get('Estado'),
            id_habitaciones=data.get('id_habitaciones')
        )
        affected = MantenimientoModel.update_mantenimiento(mantenimiento)
        if affected == 1:
            return jsonify({'message': 'Mantenimiento actualizado'}), 200
        else:
            return jsonify({'error': 'No se pudo actualizar'}), 400
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500

@main.route('delete/<uuid:id>', methods=['DELETE'])
def delete_mantenimiento(id):
    try:
        mantenimiento = Mantenimiento(
            id_mantenimiento=str(id),
            FechaSolicitud=datetime.now(),
            DescripcionProblema="",
            FechaResolucion=datetime.now(),
            Estado="",
            id_habitaciones=""
        )
        affected = MantenimientoModel.delete_mantenimiento(mantenimiento)
        if affected == 1:
            return jsonify({'message': f'Mantenimiento {id} eliminado'}), 200
        else:
            return jsonify({'error': 'No encontrado'}), 404
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500
