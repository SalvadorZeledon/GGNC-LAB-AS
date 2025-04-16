from flask import Blueprint, request, jsonify
import uuid
from ..models.EstudiantesModel import EstudiantesModel
from ..models.entities.Estudiantes import Estudiantes
from utils.DateFormat import DateFormat  # ← Aquí se importa
from datetime import datetime

main = Blueprint('estudiantes_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_estudiantes():
    try:
        estudiantes = EstudiantesModel.get_all_estudiantes()
        return jsonify(estudiantes), 200
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500

@main.route('/<uuid:id>', methods=['GET'])
def get_estudiante(id):
    try:
        estudiante = EstudiantesModel.get_estudiante_by_id(str(id))
        if estudiante:
            return jsonify(estudiante), 200
        else:
            return jsonify({'message': 'Estudiante no encontrado'}), 404
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_estudiante():
    try:
        data = request.get_json()
        required_fields = ['Nombre', 'Apellido', 'Carnet']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Faltan campos obligatorios'}), 400

        fecha_nac =  datetime.strptime(data.get('FechaNacimiento'), '%d/%m/%Y')

        estudiante = Estudiantes(
            id_estudiantes=str(uuid.uuid4()),
            Nombre=data['Nombre'],
            Apellido=data['Apellido'],
            Carnet=data['Carnet'],
            FechaNacimiento=fecha_nac,
            Genero=data.get('Genero'),
            Carrera=data.get('Carrera'),
            Telefono=data.get('Telefono'),
            Email=data.get('Email')
        )
        EstudiantesModel.add_estudiante(estudiante)
        return jsonify({'message': 'Estudiante agregado'}), 201
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500

@main.route('update/<uuid:id>', methods=['PUT'])
def update_estudiante(id):
    try:
        data = request.get_json()
        
        fecha_nac =  datetime.strptime(data.get('FechaNacimiento'), '%d/%m/%Y')

        estudiante = Estudiantes(
            id_estudiantes=str(id),
            Nombre=data.get('Nombre'),
            Apellido=data.get('Apellido'),
            Carnet=data.get('Carnet'),
            FechaNacimiento=fecha_nac,
            Genero=data.get('Genero'),
            Carrera=data.get('Carrera'),
            Telefono=data.get('Telefono'),
            Email=data.get('Email')
        )
        affected = EstudiantesModel.update_estudiante(estudiante)
        if affected == 1:
            return jsonify({'message': 'Estudiante actualizado'}), 200
        else:
            return jsonify({'error': 'No se pudo actualizar'}), 400
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500

@main.route('delete/<uuid:id>', methods=['DELETE'])
def delete_estudiante(id):
    try:
        estudiante = Estudiantes(
            id_estudiantes=str(id), 
            Nombre="", 
            Apellido="", 
            Carnet="",
            FechaNacimiento=datetime.now(), 
            Genero="", 
            Carrera="", 
            Telefono="", 
            Email=""
        )
        affected = EstudiantesModel.delete_estudiante(estudiante)
        if affected == 1:
            return jsonify({'message': f'Estudiante {id} eliminado'}), 200
        else:
            return jsonify({'error': 'Estudiante no encontrado'}), 404
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500
