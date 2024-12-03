from flask import Blueprint, request, jsonify
from controllers.EnviosController import EnviosController

# Instancia de Blueprint y del controlador de envíos
envios_blueprint = Blueprint('envios', __name__)
envios_controller = EnviosController()

# Ruta para agregar un envío (POST)
@envios_blueprint.route('/envios', methods=['POST'])
def agregar_envio():
    return envios_controller.agregar_envio()

# Ruta para obtener el siguiente envío en la cola sin procesarlo (GET)
@envios_blueprint.route('/envios/ver_siguiente', methods=['GET'])
def ver_siguiente_envio():
    return envios_controller.ver_siguiente_envio()

# Ruta para enviar el siguiente envío en la cola (POST)
@envios_blueprint.route('/envios/enviar', methods=['POST'])
def enviar_envio():
    return envios_controller.enviar_envio()

# Ruta para eliminar un envío específico (POST)
@envios_blueprint.route('/envios/eliminar/<int:envio_id>', methods=['POST'])
def eliminar_envio(envio_id):
    return envios_controller.eliminar_envio(envio_id)

# Ruta para obtener todos los envíos en la cola (GET)
@envios_blueprint.route('/envios', methods=['GET'])
def mostrar_envios():
    return envios_controller.mostrar_envios()

# Ruta para obtener todos los envíos (GET)
@envios_blueprint.route('/envios/todos', methods=['GET'])
def mostrar_todos_envios():
    return envios_controller.mostrar_todos_envios()

# Ruta para agregar un envío al heap con prioridad
@envios_blueprint.route('/envios/prioridad', methods=['POST'])
def agregar_envio_con_prioridad():
    data = request.get_json()
    envio_id = data.get("envio_id")
    prioridad = data.get("prioridad")
    envios_controller.agregar_envio_con_prioridad(envio_id, prioridad)
    return jsonify({"message": "Envio agregado con prioridad"}), 201

# Ruta para obtener el envío con mayor prioridad sin extraerlo
@envios_blueprint.route('/envios/mayor_prioridad', methods=['GET'])
def obtener_envio_con_mayor_prioridad():
    envio = envios_controller.obtener_envio_con_mayor_prioridad()
    return jsonify(envio), 200

# Ruta para extraer el envío con mayor prioridad
@envios_blueprint.route('/envios/extraer_mayor_prioridad', methods=['DELETE'])
def extraer_envio_con_mayor_prioridad():
    envio = envios_controller.extraer_envio_con_mayor_prioridad()
    return jsonify(envio), 200

# Ruta para mostrar todos los envíos en el heap de acuerdo a su prioridad
@envios_blueprint.route('/envios/priorizados', methods=['GET'])
def mostrar_todos_los_envios_priorizados():
    envios = envios_controller.mostrar_todos_los_envios_priorizados()
    return jsonify({"envios": envios}), 200

@envios_blueprint.route('/envios/enviar_mayor_prioridad', methods=['POST'])
def enviar_envio_con_mayor_prioridad():
    return envios_controller.enviar_envio_con_mayor_prioridad()

# Ruta para obtener un envio específico de la base de datos (GET)
@envios_blueprint.route('/envios/<int:envio_id>', methods=['GET'])
def obtener_envio_id(envio_id):
    return envios_controller.obtener_envio_id(envio_id)
