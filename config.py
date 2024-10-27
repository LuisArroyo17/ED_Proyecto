# config.py
import os
import pymysql  # Agrega esta línea para importar pymysql
from dotenv import load_dotenv

load_dotenv()  # Cargar las variables de entorno desde el archivo .env

class Config:
    DEBUG = True
    SECRET_KEY = 'your_secret_key_here'
    
    DB_CONFIG = {
        'host': os.getenv("DATABASE_HOST", "localhost"),
        'user': os.getenv("DATABASE_USER", "root"),
        'password': os.getenv("DATABASE_PASSWORD", "140401"),
        'database': os.getenv("DATABASE_NAME", "ed-db"),
        'cursorclass': pymysql.cursors.DictCursor  # Ahora pymysql está definido
    }
