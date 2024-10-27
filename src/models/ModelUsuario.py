from utils.db import get_connection  # Importa get_connection en lugar de DB

class ModelUsuario:
    def __init__(self):
        self.db = get_connection()  # Usa get_connection() directamente

    def __del__(self):
        if self.db:
            self.db.close()

    def agregar_usuarioDB(self, nombre, email, contrasena, rol):
        cursor = self.db.cursor()
        try:
            cursor.execute("""
                INSERT INTO usuarios (nombre, email, contrasena, rol)
                VALUES (%s, %s, %s, %s);
            """, (nombre, email, contrasena, rol))
            self.db.commit()
            return {"last_row_id": cursor.lastrowid, "row_count": cursor.rowcount}, 201
        except Exception as e:
            return {"status": "error", "message": str(e)}, 500

    def obtener_usuarioDB(self, id):
        cursor = self.db.cursor()
        try:
            cursor.execute("SELECT * FROM usuarios WHERE id = %s;", (id,))
            usuario = cursor.fetchone()
            if usuario:
                return {"data": usuario}, 200
            else:
                return {"message": "Usuario no encontrado"}, 404
        except Exception as e:
            return {"status": "error", "message": str(e)}, 500

    def actualizar_usuarioDB(self, id, nombre, email, rol):
        cursor = self.db.cursor()
        try:
            cursor.execute("""
                UPDATE usuarios SET nombre=%s, email=%s, rol=%s WHERE id=%s;
            """, (nombre, email, rol, id))
            self.db.commit()
            return {"message": "Usuario actualizado", "row_count": cursor.rowcount}, 200
        except Exception as e:
            return {"status": "error", "message": str(e)}, 500

    def eliminar_usuarioDB(self, id):
        cursor = self.db.cursor()
        try:
            cursor.execute("DELETE FROM usuarios WHERE id = %s;", (id,))
            self.db.commit()
            return {"message": "Usuario eliminado", "row_count": cursor.rowcount}, 200
        except Exception as e:
            return {"status": "error", "message": str(e)}, 500
