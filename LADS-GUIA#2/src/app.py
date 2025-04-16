from flask import Flask
from flask_cors import CORS
from Config.config import app_config 
from APIS.Contratos.routes.Contratos import main as contrato_main 
from APIS.Edificios.routes.Edificios import main as edificios_blueprint
from APIS.Estudiantes.routes.Estudiantes import main as estudiantes_blueprint
from APIS.Habitaciones.routes.Habitaciones import main as habitaciones_blueprint
from APIS.Mantenimiento.routes.Mantenimiento import main as mantenimiento_blueprint
from APIS.Pagos.routes.Pagos import main as pagos_blueprint
from APIS.Quejas.routes.Quejas import main as quejas_blueprint
from APIS.Reportes.routes.Reportes import main as reportes_blueprint
from APIS.Visitantes.routes.Visitantes import main as visitantes_blueprint
from APIS.telefonos.routes.Telefonos import main as telefonos_blueprint
from APIS.notificaciones.routes.Notificaciones import main as notificaciones_blueprint


app = Flask(__name__)
CORS(app)

def paginaNoEncontrada(error):
    return "<h1>Pagina no encontrada</h1>", 404

def errorServidor(error):
    return "<h1>Error interno del servidor</h1>", 500

@app.route('/')
def principal():
    return "<h1>Bienvenidos a mi app con Flask</h1>"

if __name__ == '__main__':
    app.config.from_object(app_config['development'])
    app.register_error_handler(404, paginaNoEncontrada)
    app.register_error_handler(500, errorServidor)
    app.register_blueprint(contrato_main, url_prefix="/APIS/Contratos")
    app.register_blueprint(edificios_blueprint, url_prefix='/APIS/Edificios')
    app.register_blueprint(estudiantes_blueprint, url_prefix='/APIS/Estudiantes')
    app.register_blueprint(habitaciones_blueprint, url_prefix='/APIS/Habitaciones')
    app.register_blueprint(mantenimiento_blueprint, url_prefix='/APIS/Mantenimiento')
    app.register_blueprint(pagos_blueprint, url_prefix='/APIS/Pagos')
    app.register_blueprint(quejas_blueprint, url_prefix='/APIS/Quejas')
    app.register_blueprint(reportes_blueprint, url_prefix='/APIS/Reportes')
    app.register_blueprint(visitantes_blueprint, url_prefix='/APIS/Visitantes')
    app.register_blueprint(telefonos_blueprint, url_prefix="/APIS/telefonos")
    app.register_blueprint(notificaciones_blueprint, url_prefix="/APIS/notificaciones")

    app.run(host='0.0.0.0', port=5000, debug=True)
