from utils.conectarDB import DB


class ModelProducto :
    def __init__(self)-> None:
        self.db = DB().connection()
    def __del__(self) -> None:
        if self.db:
            self.db.close()
            
    def agregar_productoDB(self, nombre, precio, categoria, descripcion):
        cursor = self.db.cursor()
        try:
            cursor.execute("""
                INSERT INTO productos (nombre, precio, categoria, descripcion)
                VALUES (%s, %s, %s, %s);
            """, (nombre, precio, categoria, descripcion))
            self.db.commit()
            return { "last_row_id": cursor.lastrowid, "row_count": cursor.rowcount }, 201
        except Exception as e:
            print(f"Error: {e}")
            # Devuelve una respuesta en caso de error
            return { "status": "error", "message": "No se pudo insertar el producto", "error": str(e) }, 500
    
    def obtener_productos(self):
        cursor = self.db.cursor()
        try:
            cursor.execute("SELECT * FROM productos;")
            response = cursor.fetchall()
            return { "data": response }
        except:
            return { "error": "Error durante la consulta a la tabla productos."}
        
    def obtener_productoDB_ID(self, id):
        cursor = self.db.cursor()
        try:
            cursor.execute("SELECT * FROM productos WHERE id = %s;", (id,))
            response = cursor.fetchone()
            if response:
                return { "data": response }
            else:
                return { "error": "Producto no encontrado." }
        except:
            return { "error": "Error durante la consulta a la tabla productos."}
    
    def actualizar_productoDB(self, id, nombre, precio, categoria, descripcion):
        cursor = self.db.cursor()
        try:
            cursor.execute("""
                UPDATE productos
                SET nombre = %s, precio = %s, categoria = %s, descripcion = %s
                WHERE id = %s;
            """, (nombre, precio, categoria, descripcion, id))
            self.db.commit()
            return { "message": "Producto actualizado." }
        except:
            return { "error": "Error durante la actualización del producto."}
    
    def eliminar_productoDB(self, id):
        cursor = self.db.cursor()
        try:
            cursor.execute("DELETE FROM productos WHERE id = %s;", (id,))
            self.db.commit()
            return { "message": "Producto eliminado." }
        except:
            return { "error": "Error durante la eliminación del producto."}