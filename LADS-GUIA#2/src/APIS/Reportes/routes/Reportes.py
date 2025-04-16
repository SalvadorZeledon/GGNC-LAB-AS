from flask import Blueprint, request, jsonify
import uuid
from ..models.ReportesModel import ReportesModel
from ..models.entities.Reportes import Reportes
from utils.DateFormat import DateFormat
from datetime import datetime

main = Blueprint('reportes_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_reportes():
    try:
        reportes = ReportesModel.get_all_reportes()
        return jsonify(reportes), 200
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500

@main.route('/<uuid:id>', methods=['GET'])
def get_reporte(id):
    try:
        reporte = ReportesModel.get_reporte_by_id(str(id))
        if reporte:
            return jsonify(reporte), 200
        else:
            return jsonify({'message': 'Reporte no encontrado'}), 404
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_reporte():
    try:
        data = request.get_json()
        if 'TipoReporte' not in data:
            return jsonify({'error': 'TipoReporte es obligatorio'}), 400
        
        reporte = Reportes(
            id_reportes=str(uuid.uuid4()),
            TipoReporte=data['TipoReporte'],
            FechaGeneracion=datetime.now(),
            Descripcion=data.get('Descripcion'),
            RutaArchivo=data.get('RutaArchivo')
        )
        ReportesModel.add_reporte(reporte)
        return jsonify({'message': 'Reporte agregado'}), 201
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500
    
@main.route('update/<uuid:id>', methods=['PUT'])
def update_reporte(id):
    try:
        data = request.get_json()

        
        if 'TipoReporte' not in data:
            return jsonify({'error': 'TipoReporte es obligatorio'}), 400

        reporte = Reportes(
            id_reportes=str(id),
            TipoReporte=data.get('TipoReporte'),
            FechaGeneracion=datetime.now(), 
            Descripcion=data.get('Descripcion'),
            RutaArchivo=data.get('RutaArchivo')
        )

        affected = ReportesModel.update_reporte(reporte)

        if affected == 1:
            return jsonify({'message': 'Reporte actualizado'}), 200
        else:
            return jsonify({'error': 'No se pudo actualizar el reporte'}), 400

    except Exception as ex:
        return jsonify({'error': str(ex)}), 500


@main.route('delete/<uuid:id>', methods=['DELETE'])
def delete_reporte(id):
    try:
        reporte = Reportes(
            id_reportes=str(id),
            TipoReporte="",
            FechaGeneracion=datetime.now(),
            Descripcion="",
            RutaArchivo=""
        )
        affected = ReportesModel.delete_reporte(reporte)
        if affected == 1:
            return jsonify({'message': f'Reporte {id} eliminado'}), 200
        else:
            return jsonify({'error': 'Reporte no encontrado'}), 404
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500
