# src/controllers/EnviosController.py
from flask import jsonify
from flask import request, jsonify
from models.ModelEnvio import ModelEnvio

class EnviosController:
    def agregar_envio(self):
         # Extrae los detalles y la prioridad del envío desde la solicitud JSON
        detalles = request.json.get("detalles")
        prioridad = request.json.get("prioridad", 0)  # Por defecto, la prioridad es 0 (no urgente)

        # Llama a ModelEnvio para agregar el envío a la base de datos
        resultado = ModelEnvio().agregar_envioDB(detalles, prioridad)

        # Retorna el resultado como respuesta JSON
        return jsonify(resultado)
        

    def actualizar_estado_envio(self, envio_id):
        nuevo_estado = request.json.get("estado")

        # Llama a ModelEnvio para actualizar el estado del envío en la base de datos
        resultado = ModelEnvio().actualizar_estado_envio(envio_id, nuevo_estado)

        # Retorna el resultado como respuesta JSON
        return jsonify(resultado)


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
