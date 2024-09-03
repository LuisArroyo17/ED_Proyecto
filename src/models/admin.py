from utils.conectarDB import DB

class AdminModel:
    def __init__(self):
        self.db = DB.connection()
        
    def __del__(self):
        if self.ed:
            self.db.close()
        
    def insertar_admin(self, username, password, first_name, last_name):
        cursor = self.db.cursor()
        try:
            cursor.execute("""
                insert into admin (username, password, first_name, last_name)
                values (%s, %s, %s, %s)
            """, (username, password, first_name, last_name))
            self.db.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error: {e}")
