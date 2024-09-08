from utils.conectarDB import DB


class Producto :
    def __init__(self):
        self.db = DB().connection()

    def agregar_producto(self, nombre, precio, stock):
        cursor = self.db.cursor()
        try:
            cursor.execute("""
                INSERT INTO productos (nombre, precio, stock)
                VALUES (%s, %s, %s)
            """, (nombre, precio, stock))
            self.db.commit()
            return { "last_row_id": cursor.lastrowid, "row_count": cursor.rowcount }, 201
        except Exception as e:
            print(f"Error: {e}")
            # Devuelve una respuesta en caso de error
            return { "status": "error", "message": "No se pudo insertar el producto", "error": str(e) }, 500