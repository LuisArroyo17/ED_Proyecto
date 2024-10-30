# utils/db.py
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
import pymysql
from config import Config

def get_connection():
    return pymysql.connect(**Config.DB_CONFIG)
