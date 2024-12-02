from flask import json
import pymysql.cursors
from utils.creartablas import DB
from utils.db import get_connection 
import pymysql
class ModelCarrito:
    def __init__(self):
        self.db = get_connection()
        
    def __del__(self):
        if self.db:
            self.db.close()    
            
    def agregar_carritoDB(self, usuario_id, producto_id, cantidad):
        cursor = self.db.cursor()
        try:
            cursor.execute("""
                INSERT INTO carrito_compras (usuario_id, producto_id, cantidad)
                VALUES (%s, %s, %s);
            """, (usuario_id, producto_id, cantidad))
            self.db.commit()
            return {"last_row_id": cursor.lastrowid, "row_count": cursor.rowcount}, 201
        except Exception as e:
            return {"status": "error", "message": str(e)}, 500
        
    def obtener_productosDB(self):
        cursor = self.db.cursor(pymysql.cursors.DictCursor)
        try:
            cursor.execute("SELECT * FROM productos")  # Consultar todos los productos
            productos = cursor.fetchall()  # Obtener todos los registros
            return productos  # Devolver la lista de productos
        except Exception as e:
            return {"status": "error", "message": str(e)}
        
    def obtener_carritoDB(self, usuario_id):
        cursor = self.db.cursor()
        try:
            cursor.execute("""
                SELECT p.id, p.nombre, p.precio, c.cantidad, p.imagen
                FROM carrito_compras c
                INNER JOIN productos p ON c.producto_id = p.id
                WHERE c.usuario_id = %s;
            """, (usuario_id,))
            productos = cursor.fetchall()
            return productos
        except Exception as e:
            return {"status": "error", "message": str(e)}