from flask import Blueprint, jsonify, request
import uuid
from ..models.ContratosModel import ContratoModel
from ..models.entities.Contratos import Contratos
from datetime import datetime

main = Blueprint('contrato_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_contratos():
    try:
        contratos = ContratoModel.get_all_contratos()
        if contratos:
            return jsonify(contratos), 200
        else:
            return jsonify({"message": "No se encontraron contratos"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500


@main.route('/<uuid:id>', methods=['GET'])
def get_contrato_by_id(id):
    try:
        contratos = ContratoModel.get_contrato_by_id(str(id))
        if contratos:
            return jsonify(contratos), 200
        else:
            return jsonify({"message": "Contrato no encontrado"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_contratos():
    try:
        data = request.get_json()
        required_fields = ['FechaInicio', 'FechaFin', 'MontoMensual', 'Estado', 'id_Estudiantes', 'id_Habitaciones']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400

        contrato_id = str(uuid.uuid4())

        FechaInicio = datetime.strptime(data.get('FechaInicio'), '%d/%m/%Y')
        FechaFin = datetime.strptime(data.get('FechaFin'), '%d/%m/%Y')

        contrato = Contratos(
            id_contratos=contrato_id,
            FechaInicio=FechaInicio,
            FechaFin=FechaFin,
            MontoMensual=data.get('MontoMensual'),
            Estado=data.get('Estado'),
            id_estudiantes=data.get('id_Estudiantes'),
            id_habitaciones=data.get('id_Habitaciones')
        )

        ContratoModel.add_contrato(contrato)
        return jsonify({"message": "Contrato agregado", "id": contrato_id}), 201

    except Exception as ex:
        return jsonify({"error": str(ex)}), 500


@main.route('/update/<uuid:id>', methods=['PUT'])
def update_contrato(id):
    try:
        data = request.get_json()
        existing_contrato = ContratoModel.get_contrato_by_id(str(id))

        if not existing_contrato:
            return jsonify({"error": "Contrato no encontrado"}), 404

        required_fields = ['FechaInicio', 'FechaFin', 'MontoMensual', 'Estado', 'id_Estudiantes', 'id_Habitaciones']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400

        fecha_inicio_obj = datetime.strptime(data.get('FechaInicio'), '%d/%m/%Y')
        fecha_fin_obj = datetime.strptime(data.get('FechaFin'), '%d/%m/%Y')

        contrato = Contratos(
            id_contratos=str(id),
            FechaInicio=fecha_inicio_obj,
            FechaFin=fecha_fin_obj,
            MontoMensual=data.get('MontoMensual'),
            Estado=data.get('Estado'),
            id_estudiantes=data.get('id_Estudiantes'),
            id_habitaciones=data.get('id_Habitaciones')
        )

        affected_rows = ContratoModel.update_contrato(contrato)

        if affected_rows == 1:
            return jsonify({"message": "Contrato actualizado correctamente"}), 200
        else:
            return jsonify({"error": "No se pudo actualizar el contrato"}), 400

    except Exception as ex:
        return jsonify({"error": str(ex)}), 500


@main.route('/delete/<uuid:id>', methods=['DELETE'])
def delete_contrato(id):
    try:
        contrato = Contratos(
            id_contratos=str(id),
            FechaInicio=datetime.now(),
            FechaFin=datetime.now(),
            MontoMensual="",
            Estado="",
            id_estudiantes="",
            id_habitaciones=""
        )

        affected_rows = ContratoModel.delete_contratos(contrato)

        if affected_rows == 1:
            return jsonify({"message": f"Contrato {id} eliminado"}), 200
        else:
            return jsonify({"error": "Contrato no encontrado"}), 404

    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
