# config.py
import os
import pymysql
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv('.envvars')

class Config:
    DEBUG = True
    SECRET_KEY = 'your_secret_key_here'

    DB_CONFIG = {
        'host': os.getenv("DATABASE_HOST", "localhost"),
        'user': os.getenv("DATABASE_USER", "root"),
        'password': os.getenv("DATABASE_PASSWORD", "tu_contraseña"),
        'database': os.getenv("DATABASE_NAME", "ed-db"),
        'cursorclass': pymysql.cursors.DictCursor
    }

print(Config.DB_CONFIG)