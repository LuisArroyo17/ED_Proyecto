# utils/db.py
import sys
print(sys.path)  # Esto mostrará el path de búsqueda de módulos de Python.
import pymysql
from config import Config  # Asegúrate de que tienes un archivo config.py con la configuración de la base de datos

def get_connection():
    return pymysql.connect(**Config.DB_CONFIG)
