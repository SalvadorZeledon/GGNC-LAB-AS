from flask import Blueprint, request, jsonify
import uuid
from ..models.HabitacionesModel import HabitacionesModel
from ..models.entities.Habitaciones import Habitaciones

main = Blueprint('habitaciones_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_habitaciones():
    try:
        habitaciones = HabitacionesModel.get_all_habitaciones()
        return jsonify(habitaciones), 200
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500

@main.route('/<uuid:id>', methods=['GET'])
def get_habitacion(id):
    try:
        habitacion = HabitacionesModel.get_habitacion_by_id(str(id))
        if habitacion:
            return jsonify(habitacion), 200
        else:
            return jsonify({'message': 'Habitación no encontrada'}), 404
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_habitacion():
    try:
        data = request.get_json()
        required_fields = ['Numero', 'id_edificios']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Faltan campos obligatorios'}), 400

        habitacion = Habitaciones(
            id_habitaciones=str(uuid.uuid4()),
            Numero=data['Numero'],
            Piso=data.get('Piso'),
            Tipo=data.get('Tipo'),
            Capacidad=data.get('Capacidad'),
            Estado=data.get('Estado'),
            id_edificios=data['id_edificios']
        )
        HabitacionesModel.add_habitacion(habitacion)
        return jsonify({'message': 'Habitación agregada'}), 201
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500

@main.route('update/<uuid:id>', methods=['PUT'])
def update_habitacion(id):
    try:
        data = request.get_json()
        habitacion = Habitaciones(
            id_habitaciones=str(id),
            Numero=data.get('Numero'),
            Piso=data.get('Piso'),
            Tipo=data.get('Tipo'),
            Capacidad=data.get('Capacidad'),
            Estado=data.get('Estado'),
            id_edificios=data.get('id_edificios')
        )
        affected = HabitacionesModel.update_habitacion(habitacion)
        if affected == 1:
            return jsonify({'message': 'Habitación actualizada'}), 200
        else:
            return jsonify({'error': 'No se pudo actualizar'}), 400
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500

@main.route('delete/<uuid:id>', methods=['DELETE'])
def delete_habitacion(id):
    try:
        habitacion = Habitaciones(
            id_habitaciones=str(id),
            Numero="", Piso=None, Tipo="", Capacidad=None, Estado="", id_edificios=""
        )
        affected = HabitacionesModel.delete_habitacion(habitacion)
        if affected == 1:
            return jsonify({'message': f'Habitación {id} eliminada'}), 200
        else:
            return jsonify({'error': 'Habitación no encontrada'}), 404
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500
