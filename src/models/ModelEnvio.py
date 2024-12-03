from utils.db import get_connection

class ModelEnvios:
    def __init__(self):
        self.db = get_connection()

    def __del__(self):
        if self.db:
            self.db.close()

    def obtener_todos_envios(self):
        cursor = self.db.cursor()
        try:
            cursor.execute("SELECT id, pedido_id, detalles, prioridad, estado FROM envios;")
            envios = cursor.fetchall()
            return envios, 200
        except Exception as e:
            return {
                "status": "error",
                "message": "Error al obtener todos los envios",
                "error": str(e)
            }, 500

    def agregar_envioDB(self, pedido_id, detalles, prioridad, estado):
        cursor = self.db.cursor()
        try:
            cursor.execute("""
                INSERT INTO envios (pedido_id, detalles, prioridad, estado)
                VALUES (%s, %s, %s, %s);
            """, (pedido_id, detalles, prioridad, estado))
            envio_id = cursor.lastrowid
            self.db.commit()
            return {
                "status": "success",
                "message": "Envio agregado",
                "data": {
                    "envio_id": envio_id,
                    "pedido_id": pedido_id,
                    "detalles": detalles,
                    "prioridad": prioridad,
                    "estado": estado
                }
            }, 201
        except Exception as e:
            self.db.rollback()
            return {
                "status": "error",
                "message": "No se pudo agregar el envio",
                "error": str(e)
            }, 500

    def obtener_envios_pendientes(self):
        cursor = self.db.cursor()
        try:
            cursor.execute("SELECT id, pedido_id, detalles, prioridad, estado FROM envios WHERE estado = 'pendiente';")
            envios = cursor.fetchall()
            return envios, 200
        except Exception as e:
            return {
                "status": "error",
                "message": "Error al obtener los envios pendientes",
                "error": str(e)
            }, 500

    def actualizar_estadoDB(self, id, estado):
        cursor = self.db.cursor()
        try:
            cursor.execute("UPDATE envios SET estado=%s WHERE id=%s;", (estado, id))
            self.db.commit()
            if cursor.rowcount > 0:
                return {
                    "status": "success",
                    "message": "Estado del envio actualizado",
                    "data": {
                        "envio_id": id,
                        "estado": estado
                    }
                }, 200
            else:
                return {
                    "status": "error",
                    "message": "Envio no encontrado"
                }, 404
        except Exception as e:
            return {
                "status": "error",
                "message": "Error al actualizar el estado del envio",
                "error": str(e)
            }, 500

    def eliminar_envioDB(self, id):
        cursor = self.db.cursor()
        try:
            cursor.execute("DELETE FROM envios WHERE id = %s;", (id,))
            self.db.commit()
            if cursor.rowcount > 0:
                return {
                    "status": "success",
                    "message": "Envio eliminado",
                    "data": {
                        "envio_id": id
                    }
                }, 200
            else:
                return {
                    "status": "error",
                    "message": "Envio no encontrado"
                }, 404
        except Exception as e:
            return {
                "status": "error",
                "message": "Error al eliminar el envio",
                "error": str(e)
            }, 500
        
    def obtener_envio_por_id(self, id):
        cursor = self.db.cursor()
        try:
            cursor.execute("SELECT id, pedido_id, detalles, prioridad, estado FROM envios WHERE id = %s", (id,))
            envios = cursor.fetchall()
            return envios, 200
        except Exception as e:
            print(f"Error al obtener el envío por ID: {str(e)}")
            return None
