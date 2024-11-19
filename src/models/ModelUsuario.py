import pymysql
from utils.db import get_connection  # Importa get_connection correctamente

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
            self.db.rollback()  # Asegura revertir cambios en caso de error
            return {"status": "error", "message": str(e)}, 500
        finally:
            cursor.close()

    def obtener_usuario_por_emailDB(self, email):
        cursor = self.db.cursor(pymysql.cursors.DictCursor)
        try:
            cursor.execute("""
                SELECT id, nombre, email, contrasena, rol
                FROM usuarios
                WHERE email = %s;
            """, (email,))
            usuario = cursor.fetchone()
            if usuario:
                return {"data": usuario}, 200
            else:
                return {"message": "Usuario no encontrado"}, 404
        except Exception as e:
            return {"status": "error", "message": str(e)}, 500
        finally:
            cursor.close()

    def obtener_usuarioDB(self, id):
        cursor = self.db.cursor(pymysql.cursors.DictCursor)
        try:
            cursor.execute("SELECT id, nombre, email, contrasena, rol FROM usuarios WHERE id = %s;", (id,))
            usuario = cursor.fetchone()
            if usuario:
                return {"data": usuario}, 200
            else:
                return {"message": "Usuario no encontrado"}, 404
        except Exception as e:
            return {"status": "error", "message": str(e)}, 500
        finally:
            cursor.close()

    def actualizar_usuarioDB(self, id, nombre, email, rol):
        cursor = self.db.cursor()
        try:
            cursor.execute("""
                UPDATE usuarios SET nombre=%s, email=%s, rol=%s WHERE id=%s;
            """, (nombre, email, rol, id))
            self.db.commit()
            return {"message": "Usuario actualizado", "row_count": cursor.rowcount}, 200
        except Exception as e:
            self.db.rollback()
            return {"status": "error", "message": str(e)}, 500
        finally:
            cursor.close()

    def eliminar_usuarioDB(self, id):
        cursor = self.db.cursor()
        try:
            cursor.execute("DELETE FROM usuarios WHERE id = %s;", (id,))
            self.db.commit()
            return {"message": "Usuario eliminado", "row_count": cursor.rowcount}, 200
        except Exception as e:
            self.db.rollback()
            return {"status": "error", "message": str(e)}, 500
        finally:
            cursor.close()
