from utils.creartablas import DB

class ModelPedido:
    def __init__(self):
        self.db = DB().connection()

    def __del__(self):
        if self.db:
            self.db.close()
    def agregar_pedidoDB(self, usuario_id, total, estado):
        cursor = self.db.cursor()
        try:
            cursor.execute("""
                INSERT INTO pedidos (usuario_id, total, estado)
                VALUES (%s, %s, %s);
            """, (usuario_id, total, estado))
            self.db.commit()
            return {"last_row_id": cursor.lastrowid, "row_count": cursor.rowcount}, 201
        except Exception as e:
            return {"status": "error", "message": str(e)}, 500

    def obtener_pedidoDB(self, id):
        cursor = self.db.cursor()
        try:
            cursor.execute("SELECT * FROM pedidos WHERE id = %s;", (id,))
            pedido = cursor.fetchone()
            if pedido:
                return {"data": pedido}, 200
            else:
                return {"message": "Pedido no encontrado"}, 404
        except Exception as e:
            return {"status": "error", "message": str(e)}, 500

    def actualizar_pedidoDB(self, id, total, estado):
        cursor = self.db.cursor()
        try:
            cursor.execute("""
                UPDATE pedidos SET total=%s, estado=%s WHERE id=%s;
            """, (total, estado, id))
            self.db.commit()
            return {"message": "Pedido actualizado", "row_count": cursor.rowcount}, 200
        except Exception as e:
            return {"status": "error", "message": str(e)}, 500

    def eliminar_pedidoDB(self, id):
        cursor = self.db.cursor()
        try:
            cursor.execute("DELETE FROM pedidos WHERE id = %s;", (id,))
            self.db.commit()
            return {"message": "Pedido eliminado", "row_count": cursor.rowcount}, 200
        except Exception as e:
            return {"status": "error", "message": str(e)}, 500
# asasasasasA