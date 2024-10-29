# src/models/ModelEnvio.py
from utils.db import get_connection

class ModelEnvio:
    def __init__(self):
        self.db = get_connection()

    def __del__(self):
        if self.db:
            self.db.close()

    def agregar_envioDB(self, detalles):
        # Código existente para agregar envío
        pass

    def actualizar_estado_envio(self, envio_id, estado):
        # Código existente para actualizar estado de envío
        pass

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

