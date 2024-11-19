# src/controllers/EnviosController.py
from flask import request, jsonify
from models.ModelEnvio import ModelEnvio
import heapq

class EnviosController:
    def __init__(self):
        # Cola de prioridad: almacenará los envíos como (prioridad, detalles) usando heapq
        self.envios_prioritarios = []

    def agregar_envio(self):
        # Extrae los detalles y la prioridad del envío desde la solicitud JSON
        detalles = request.json.get("detalles")
        prioridad = request.json.get("prioridad", 0)  # Por defecto, la prioridad es 0 (no urgente)
        
        # Agrega a la cola de prioridad usando el valor de prioridad
        heapq.heappush(self.envios_prioritarios, (prioridad, detalles))
        
        # También lo almacena en la base de datos
        resultado = ModelEnvio().agregar_envioDB(detalles, prioridad)
        
        # Retorna el resultado como respuesta JSON
        return jsonify(resultado)

    def obtener_siguiente_envio(self):
        # Obtiene el siguiente envío de la cola de prioridad (el de mayor prioridad)
        if self.envios_prioritarios:
            prioridad, detalles = heapq.heappop(self.envios_prioritarios)
            return jsonify({"prioridad": prioridad, "detalles": detalles}), 200
        else:
            return jsonify({"message": "No hay envíos pendientes"}), 404

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