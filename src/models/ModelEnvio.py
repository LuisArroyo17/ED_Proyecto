# src/models/ModelEnvio.py
from utils.db import get_connection
from flask import request, jsonify

class ModelEnvio:
    def __init__(self):
        self.db = get_connection()

    def __del__(self):
        if self.db:
            self.db.close()

    def agregar_envioDB(self, detalles):
         # Extrae los detalles y la prioridad del envío desde la solicitud JSON
        detalles = request.json.get("detalles")
        prioridad = request.json.get("prioridad", 0)  # Por defecto, la prioridad es 0 (no urgente)

        # Llama a ModelEnvio para agregar el envío a la base de datos
        resultado = ModelEnvio().agregar_envioDB(detalles, prioridad)

        # Retorna el resultado como respuesta JSON
        return jsonify(resultado)

    def actualizar_estado_envio(self, envio_id, estado):
        nuevo_estado = request.json.get("estado")

        # Llama a ModelEnvio para actualizar el estado del envío en la base de datos
        resultado = ModelEnvio().actualizar_estado_envio(envio_id, nuevo_estado)

        # Retorna el resultado como respuesta JSON
        return jsonify(resultado)

    def obtener_envios(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM envios")
        envios = cursor.fetchall()
        return envios

    def obtener_envio(self, envio_id):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM envios WHERE id = %s", (envio_id,))
        envio = cursor.fetchone()
        return envio

    def eliminar_envioDB(self, envio_id):
        cursor = self.db.cursor()
        cursor.execute("DELETE FROM envios WHERE id = %s", (envio_id,))
        self.db.commit()
        if cursor.rowcount > 0:
            return {"message": "Envío eliminado"}, 200
        return {"message": "Envío no encontrado"}, 404
