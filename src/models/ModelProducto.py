# models/ModelProductos.py
from utils.db import get_connection  # Usamos get_connection en lugar de DB

class ModelProducto:
    def __init__(self):
        self.db = get_connection()  # Usamos get_connection directamente

    def __del__(self):
        if self.db:
            self.db.close()

    def agregar_productoDB(self, nombre, precio, categoria, descripcion, stock, imagen_path):
        cursor = self.db.cursor()
        try:
            cursor.execute("""
                INSERT INTO productos (nombre, precio, categoria, descripcion, stock, imagen)
                VALUES (%s, %s, %s, %s, %s, %s);
            """, (nombre, precio, categoria, descripcion, stock, imagen_path))
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

    # def obtener_productos(self, offset=0, limit=10, categoria=None):
    #     cursor = self.db.cursor()  # Usa el cursor de self.db directamente

    #     # Construir la consulta SQL con paginación y filtro opcional
    #     if categoria:
    #         query = "SELECT * FROM productos WHERE categoria = %s LIMIT %s OFFSET %s"
    #         cursor.execute(query, (categoria, limit, offset))
    #     else:
    #         query = "SELECT * FROM productos LIMIT %s OFFSET %s"
    #         cursor.execute(query, (limit, offset))

    #     productos = cursor.fetchall()
    #     return {"data": productos}, 200  # Devuelve productos en un formato consistente

    # limitado a 10(error)
    # def obtener_productos(self, offset=0, limit=10, categoria=None):
    #     cursor = self.db.cursor()
    #     if categoria:
    #         query = "SELECT * FROM productos WHERE categoria = %s LIMIT %s OFFSET %s"
    #         cursor.execute(query, (categoria, limit, offset))
    #     else:
    #         query = "SELECT * FROM productos LIMIT %s OFFSET %s"
    #         cursor.execute(query, (limit, offset))
    #     productos = cursor.fetchall()
    #     return productos  # Asegúrate de que este resultado es lo que necesitas

    def obtener_productos(self, offset=None, limit=None, categoria=None):
        cursor = self.db.cursor()
        
        # Construye la consulta SQL
        if categoria:
            query = "SELECT * FROM productos WHERE categoria = %s"
            params = (categoria,)
        else:
            query = "SELECT * FROM productos"
            params = ()
        
        # Aplica límites de paginación si se proporcionan
        if limit is not None and offset is not None:
            query += " LIMIT %s OFFSET %s"
            params += (limit, offset)

        cursor.execute(query, params)
        productos = cursor.fetchall()
        return productos
    def obtener_todos_productosDB(self):
        cursor = self.db.cursor()
        try:
            cursor.execute("SELECT id, nombre, precio, categoria, descripcion, stock FROM productos;")
            productos = cursor.fetchall()
            if productos: 
                return {"data": productos}, 200
            else: 
                return {"message": "No hay productos"}, 404
        except Exception as e:
            return {"status": "error", "message": str(e)}, 500
