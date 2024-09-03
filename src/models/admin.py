from utils.conectarDB import DB


class AdminModel:
    def __init__(self) -> None:
        self.db = DB().connection()

    def __del__(self) -> None:
        if self.db:
            self.db.close()

    def insertar_adminDB(self, username, password, first_name, last_name):
        cursor = self.db.cursor()
        try:
            cursor.execute("""
                INSERT INTO admin (username, password, first_name, last_name)
                VALUES (%s, %s, %s, %s)
            """, (username, password, first_name, last_name))
            self.db.commit()
            return { "last_row_id": cursor.lastrowid, "row_count": cursor.rowcount }, 201
        except Exception as e:
            print(f"Error: {e}")
            # Devuelve una respuesta en caso de error
            return { "status": "error", "message": "No se pudo insertar el admin", "error": str(e) }, 500




# class AdminModel:
#     def __init__(self) :
#         self.db = DB.connection()
        
#     def __del__(self):
#         if self.db:
#             self.db.close()
        

