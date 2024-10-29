# src/routes/envios.py
from flask import Blueprint, request, jsonify
from controllers.EnviosController import EnviosController

envios_blueprint = Blueprint('envios', __name__)
envios_controller = EnviosController()

@envios_blueprint.route('/envios', methods=['POST']) 
def agregar_envio():
    return envios_controller.agregar_envio()

@envios_blueprint.route('/envios/<int:envio_id>', methods=['PUT'])
def actualizar_estado_envio(envio_id):
    return envios_controller.actualizar_estado_envio(envio_id)

# Nuevo: Ruta para obtener un envío específico
@envios_blueprint.route('/envios/<int:envio_id>', methods=['GET'])
def obtener_envio(envio_id):
    return envios_controller.obtener_envio(envio_id)

# Nuevo: Ruta para eliminar un envío específico
@envios_blueprint.route('/envios/<int:envio_id>', methods=['DELETE'])
def eliminar_envio(envio_id):
    return envios_controller.eliminar_envio(envio_id)

