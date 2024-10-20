from utils.creartablas import DB


class ModelProducto:
    def __init__(self):
        self.db = DB().connection()

    def __del__(self):
        if self.db:
            self.db.close()
    def agregar_productoDB(self, nombre, precio, categoria, descripcion, stock):
        cursor = self.db.cursor()
        try:
            cursor.execute("""
                INSERT INTO productos (nombre, precio, categoria, descripcion, stock)
                VALUES (%s, %s, %s, %s, %s);
            """, (nombre, precio, categoria, descripcion, stock))
            self.db.commit()
            return {"last_row_id": cursor.lastrowid, "row_count": cursor.rowcount}, 201
        except Exception as e:
            print(f"Error: {e}")
            return {"status": "error", "message": "No se pudo insertar el producto", "error": str(e)}, 500

    def obtener_productoDB(self, id):
        cursor = self.db.cursor()
        try:
            cursor.execute("SELECT * FROM productos WHERE id = %s;", (id,))
            producto = cursor.fetchone()
            if producto:
                return {"data": producto}, 200
            else:
                return {"message": "Producto no encontrado"}, 404
        except Exception as e:
            return {"status": "error", "message": str(e)}, 500

    def actualizar_productoDB(self, id, nombre, precio, categoria, descripcion, stock):
        cursor = self.db.cursor()
        try:
            cursor.execute("""
                UPDATE productos SET nombre=%s, precio=%s, categoria=%s, descripcion=%s, stock=%s
                WHERE id=%s;
            """, (nombre, precio, categoria, descripcion, stock, id))
            self.db.commit()
            return {"message": "Producto actualizado", "row_count": cursor.rowcount}, 200
        except Exception as e:
            return {"status": "error", "message": str(e)}, 500

    def eliminar_productoDB(self, id):
        cursor = self.db.cursor()
        try:
            cursor.execute("DELETE FROM productos WHERE id = %s;", (id,))
            self.db.commit()
            return {"message": "Producto eliminado", "row_count": cursor.rowcount}, 200
        except Exception as e:
            return {"status": "error", "message": str(e)}, 500
