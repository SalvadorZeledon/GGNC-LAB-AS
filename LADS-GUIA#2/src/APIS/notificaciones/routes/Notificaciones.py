from flask import Blueprint, jsonify, request
import uuid
from datetime import datetime
from ..models.entities.Notificaciones import Notificaciones
from ..models.NotificacionesModel import NotificacionesModel
from ...telefonos.models.TelefonosModel import TelefonoModel
from ..services.servicesTwilio import send_whatsapp_message
from ..services.consulta_notificaciones import get_notification_data

main = Blueprint('notificaciones_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_notificaciones():
    try:
        notificaciones = NotificacionesModel.get_all_notificaciones()
        return jsonify(notificaciones), 200
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500


@main.route('/<id>', methods=['GET'])
def get_notificacion_by_id(id):
    try:
        notificacion = NotificacionesModel.get_notificacion_by_id(id)
        if notificacion:
            return jsonify(notificacion), 200
        else:
            return jsonify({"error": "Notificación no encontrada"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
    


@main.route('/add', methods=['POST'])
def add_notificacion():
    try:
        data = request.get_json()
        required_fields = ['id_estudiantes', 'fecha_envio', 'estado']
        missing_fields = [field for field in required_fields if field not in data]

        if missing_fields:
            return jsonify({
                "error": "Faltan campos obligatorios: " + ", ".join(missing_fields)
            }), 400

        # Extraer y validar campos
        id_estudiantes = data.get('id_estudiantes')
        fecha_envio_str = data.get('fecha_envio')
        estado = data.get('estado')

        try:
            fecha_envio = datetime.strptime(fecha_envio_str, "%Y-%m-%d")
        except Exception:
            return jsonify({
                "error": "Formato de fecha_envio inválido, se requiere YYYY-MM-DD"
            }), 400

        # Obtener datos del estudiante
        estudiante_data = get_notification_data(id_estudiantes)
        if estudiante_data:
            est = estudiante_data[0]
            message_body = (
                f"📢 Notificación para el estudiante:\n"
                f"👤 Nombre: {est.get('nombre_estudiante', 'N/A')} {est.get('apellido_estudiante', '')}\n"
                f"🎓 Carnet: {est.get('carnet', 'N/A')}\n"
                f"📧 Correo: {est.get('correo', 'N/A')}\n"
                f"📅 Fecha de envío: {fecha_envio_str}\n"
                f"📌 Estado: {estado}"
            )
        else:
            message_body = "No se encontraron datos del estudiante para esta notificación."

        # Crear la notificación con mensaje
        notificacion_id = str(uuid.uuid4())
        notificacion = Notificaciones(
            id_notificaciones=notificacion_id,
            id_estudiantes=id_estudiantes,
            fecha_envio=fecha_envio,
            estado=estado,
            mensaje=message_body  # ✅ Ahora sí lo incluye
        )

        affected_rows = NotificacionesModel.add_notificacion(notificacion)
        if affected_rows != 1:
            return jsonify({"error": "No se pudo agregar la notificación"}), 500

        # Obtener lista de teléfonos desde la tabla telefonos
        telefonos = TelefonoModel.get_all_telefonos()
        if not telefonos:
            return jsonify({"error": "No se encontraron destinatarios registrados"}), 404

        # Enviar mensaje a cada número
        send_results = {}

        for tel in telefonos:
            numero = str(tel.get("numero_telefono", "")).strip()
            if not numero:
                send_results["Número no definido"] = {
                    "status": "Error",
                    "error": "Número de teléfono vacío"
                }
                continue

            if not numero.startswith('+'):
                phone_number = "+503" + numero
            else:
                phone_number = numero

            try:
                sid = send_whatsapp_message(phone_number, message_body)
                send_results[phone_number] = {
                    "status": "Enviado",
                    "sid": sid
                }
            except Exception as e:
                send_results[phone_number] = {
                    "status": "Error",
                    "error": str(e)
                }

        return jsonify({
            "id_notificacion": notificacion.id_notificaciones,
            "message": "Notificación agregada y mensajes enviados",
            "send_results": send_results
        }), 200

    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
