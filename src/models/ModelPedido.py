from utils.db import get_connection 

class ModelPedido:
    def __init__(self):
        self.db = get_connection() 

    def __del__(self):
        if self.db:
            self.db.close()
    def obtener_todos_pedidos(self):
        cursor = self.db.cursor()
        try:
            cursor.execute("SELECT id, usuario_id, fecha, total, estado, prioridad FROM pedidos;")
            pedidos = cursor.fetchall()  
            return pedidos, 200
        except Exception as e:
            return {
                "status": "error",
                "message": "Error al obtener todos los pedidos",
                "error": str(e)
            }, 500
            
    def agregar_pedidoDB(self, usuario_id, total, estado, detalles, prioridad):
        cursor = self.db.cursor()
        try:
            cursor.execute("SELECT id FROM usuarios WHERE id = %s;", (usuario_id,))
            usuario = cursor.fetchone()
            if not usuario:
                return {
                    "status": "error",
                    "message": "El usuario no existe",
                    "error": f"Usuario con id {usuario_id} no encontrado"
                }, 400
            cursor.execute("""
                INSERT INTO pedidos (usuario_id, total, estado, prioridad)
                VALUES (%s, %s, %s, %s);
            """, (usuario_id, total, estado, prioridad))
            pedido_id = cursor.lastrowid  

            for detalle in detalles:
                producto_id = detalle['producto_id']
                cantidad = detalle['cantidad']
                precio = detalle['precio']
                cursor.execute("""
                    INSERT INTO detalle_pedidos (pedido_id, producto_id, cantidad, precio)
                    VALUES (%s, %s, %s, %s);
                """, (pedido_id, producto_id, cantidad, precio))

            self.db.commit()
            return {
                "status": "success",
                "message": "Pedido y detalles agregados",
                "data": {
                    "pedido_id": pedido_id,
                    "total": total,
                    "estado": estado,
                    "detalles": detalles,
                    "prioridad": prioridad
                }
            }, 201
        except Exception as e:
            self.db.rollback()  
            print(e)
            return {
                "status": "error",
                "message": "No se pudo agregar el pedido",
                "error": str(e)
            }, 500
            
    def obtener_pedidos_pendientes(self):
        cursor = self.db.cursor()
        try:
            cursor.execute("SELECT id, usuario_id, fecha, total, prioridad, estado FROM pedidos WHERE estado = 'pendiente';")
            pedidos = cursor.fetchall()  
            return pedidos, 200
        except Exception as e:
            return {
                "status": "error",
                "message": "Error al obtener los pedidos pendientes",
                "error": str(e)
            }, 500

    def actualizar_pedidoDB(self, id, total, estado):
        cursor = self.db.cursor()
        try:
            cursor.execute("""
                UPDATE pedidos SET total=%s, estado=%s WHERE id=%s;
            """, (total, estado, id))
            self.db.commit()
            if cursor.rowcount > 0:
                return {
                    "status": "success",
                    "message": "Pedido actualizado",
                    "data": {
                        "pedido_id": id,
                        "total": total,
                        "estado": estado
                    }
                }, 200
            else:
                return {
                    "status": "error",
                    "message": "Pedido no encontrado"
                }, 404
        except Exception as e:
            return {
                "status": "error",
                "message": "Error al actualizar el pedido",
                "error": str(e)
            }, 500

    def eliminar_pedidoDB(self, id):
        cursor = self.db.cursor()
        try:
            cursor.execute("DELETE FROM pedidos WHERE id = %s;", (id,))
            self.db.commit()
            if cursor.rowcount > 0:
                return {
                    "status": "success",
                    "message": "Pedido eliminado",
                    "data": {
                        "pedido_id": id
                    }
                }, 200
            else:
                return {
                    "status": "error",
                    "message": "Pedido no encontrado"
                }, 404
        except Exception as e:
            return {
                "status": "error",
                "message": "Error al eliminar el pedido",
                "error": str(e)
            }, 500
    def obtener_detalles_pedido(self, pedido_id):
        cursor = self.db.cursor()
        try:
            cursor.execute("""
                SELECT dp.id, dp.pedido_id, dp.producto_id, dp.cantidad, dp.precio, p.nombre AS producto_nombre
                FROM detalle_pedidos dp
                JOIN productos p ON dp.producto_id = p.id
                WHERE dp.pedido_id = %s;
            """, (pedido_id,))
            detalles = cursor.fetchall()
            return detalles, 200
        except Exception as e:
            return {
                "status": "error",
                "message": "Error al obtener los detalles del pedido",
                "error": str(e)
            }, 500
