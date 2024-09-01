import pymysql
import pymysql.cursors
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".envvars")

class DB:
    def __init__(self):
        db= self.connection()
        try:
            cursor = db.cursor()
            cursor.execute("SHOW TABLES;")
            db_tables = cursor.fetchall()
            if (db_tables.__len__() > 0):
                print("Tablas ya existen")
            else:
                self.crear_tablas()
        except Exception as e:
            print(f"Error {e}")
    def connection(self):
        db = pymysql.connections.Connection(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            cursorclass=pymysql.cursors.DictCursor
        )