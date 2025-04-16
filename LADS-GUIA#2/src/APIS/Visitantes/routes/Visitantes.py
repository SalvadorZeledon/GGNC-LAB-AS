from flask import Blueprint, request, jsonify
import uuid
from ..models.VisitantesModel import VisitantesModel
from ..models.entities.Visitantes import Visitantes
from utils.DateFormat import DateFormat
from datetime import datetime

main = Blueprint('visitantes_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_visitantes():
    try:
        visitantes = VisitantesModel.get_all_visitantes()
        return jsonify(visitantes), 200
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500

@main.route('/<uuid:id>', methods=['GET'])
def get_visitante(id):
    try:
        visitante = VisitantesModel.get_visitante_by_id(str(id))
        if visitante:
            return jsonify(visitante), 200
        else:
            return jsonify({'message': 'Visitante no encontrado'}), 404
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_visitante():
    try:
        data = request.get_json()
        if 'Nombre' not in data or 'id_estudiantes' not in data:
            return jsonify({'error': 'Campos obligatorios faltantes'}), 400

        visitante = Visitantes(
            id_visitantes=str(uuid.uuid4()),
            Nombre=data['Nombre'],
            Apellido=data.get('Apellido'),
            DUI=data.get('DUI'),
            FechaVisita=datetime.now(),
            id_estudiantes=data['id_estudiantes']
        )
        VisitantesModel.add_visitante(visitante)
        return jsonify({'message': 'Visitante agregado'}), 201
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500

@main.route('update/<uuid:id>', methods=['PUT'])
def update_visitante(id):
    try:
        data = request.get_json()

        # Validar campos necesarios
        if 'Nombre' not in data or 'id_estudiantes' not in data:
            return jsonify({'error': 'Campos obligatorios faltantes'}), 400

        visitante = Visitantes(
            id_visitantes=str(id),
            Nombre=data.get('Nombre'),
            Apellido=data.get('Apellido'),
            DUI=data.get('DUI'),
            FechaVisita=datetime.now(), 
            id_estudiantes=data.get('id_estudiantes')
        )

        affected = VisitantesModel.update_visitante(visitante)

        if affected == 1:
            return jsonify({'message': 'Visitante actualizado'}), 200
        else:
            return jsonify({'error': 'No se pudo actualizar el visitante'}), 400

    except Exception as ex:
        return jsonify({'error': str(ex)}), 500


@main.route('delete/<uuid:id>', methods=['DELETE'])
def delete_visitante(id):
    try:
        visitante = Visitantes(
            id_visitantes=str(id),
            Nombre="",
            Apellido="",
            DUI="",
            FechaVisita=datetime.now(),
            id_estudiantes=""
        )
        affected = VisitantesModel.delete_visitante(visitante)
        if affected == 1:
            return jsonify({'message': f'Visitante {id} eliminado'}), 200
        else:
            return jsonify({'error': 'Visitante no encontrado'}), 404
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500
