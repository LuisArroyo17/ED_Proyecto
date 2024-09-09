from utils.conectarDB import DB


class ModelProducto :
    def __init__(self):
        self.db = DB().connection()

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