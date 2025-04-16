from flask import Blueprint, request, jsonify
import uuid
from ..models.PagosModel import PagosModel
from ..models.entities.Pagos import Pagos
from utils.DateFormat import DateFormat
from datetime import datetime

main = Blueprint('pagos_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_pagos():
    try:
        pagos = PagosModel.get_all_pagos()
        return jsonify(pagos), 200
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500

@main.route('/<uuid:id>', methods=['GET'])
def get_pago(id):
    try:
        pago = PagosModel.get_pago_by_id(str(id))
        if pago:
            return jsonify(pago), 200
        else:
            return jsonify({'message': 'Pago no encontrado'}), 404
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_pago():
    try:
        data = request.get_json()
        if 'FechaPago' not in data or 'Monto' not in data or 'id_contratos' not in data:
            return jsonify({'error': 'Faltan campos obligatorios'}), 400

        fecha_pago =  datetime.strptime(data.get('FechaPago'), '%d/%m/%Y')
        pago = Pagos(
            id_pagos=str(uuid.uuid4()),
            FechaPago=fecha_pago,
            Monto=data['Monto'],
            MetodoPago=data.get('MetodoPago'),
            EstadoPago=data.get('EstadoPago'),
            id_contratos=data['id_contratos']
        )
        PagosModel.add_pago(pago)
        return jsonify({'message': 'Pago agregado'}), 201
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500

@main.route('update/<uuid:id>', methods=['PUT'])
def update_pago(id):
    try:
        data = request.get_json()
        fecha_pago =  datetime.strptime(data.get('FechaPago'), '%d/%m/%Y')
        pago = Pagos(
            id_pagos=str(id),
            FechaPago=fecha_pago,
            Monto=data['Monto'],
            MetodoPago=data.get('MetodoPago'),
            EstadoPago=data.get('EstadoPago'),
            id_contratos=data.get('id_contratos')
        )
        affected = PagosModel.update_pago(pago)
        if affected == 1:
            return jsonify({'message': 'Pago actualizado'}), 200
        else:
            return jsonify({'error': 'No se pudo actualizar'}), 400
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500

@main.route('delete/<uuid:id>', methods=['DELETE'])
def delete_pago(id):
    try:
        pago = Pagos(
            id_pagos=str(id),
            FechaPago=datetime.now(),
            Monto=None,
            MetodoPago="",
            EstadoPago="",
            id_contratos=""
        )
        affected = PagosModel.delete_pago(pago)
        if affected == 1:
            return jsonify({'message': f'Pago {id} eliminado'}), 200
        else:
            return jsonify({'error': 'Pago no encontrado'}), 404
    except Exception as ex:
        return jsonify({'error': str(ex)}), 500
