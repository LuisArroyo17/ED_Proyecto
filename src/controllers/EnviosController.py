# src/controllers/EnviosController.py
from flask import jsonify
from models.ModelEnvio import ModelEnvio

class EnviosController:
    def agregar_envio(self):
        # Código existente para agregar envío
        pass

    def actualizar_estado_envio(self, envio_id):
        # Código existente para actualizar estado de envío
        pass

    def obtener_envio(self, envio_id):
        # Llama a ModelEnvio para obtener un envío específico
        envio = ModelEnvio().obtener_envio(envio_id)
        if envio:
            return jsonify({"data": envio}), 200
        return jsonify({"message": "Envio no encontrado"}), 404

    def eliminar_envio(self, envio_id):
        # Llama a ModelEnvio para eliminar un envío específico
        resultado = ModelEnvio().eliminar_envioDB(envio_id)
        return jsonify(resultado)
