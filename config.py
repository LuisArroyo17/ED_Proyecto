import os
import pymysql  
from dotenv import load_dotenv

load_dotenv()  

class Config:
    DEBUG = True
    SECRET_KEY = 'your_secret_key_here'
    
    DB_CONFIG = {
        'host': os.getenv("DATABASE_HOST", "localhost"),
        'user': os.getenv("DATABASE_USER", "root"),
        'password': os.getenv("DATABASE_PASSWORD", "root"),
        'database': os.getenv("DATABASE_NAME", "ed-db"),
        'cursorclass': pymysql.cursors.DictCursor  
    }
