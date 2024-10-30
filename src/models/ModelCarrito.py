from flask import json
from utils.creartablas import DB
from utils.db import get_connection 
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
        cursor = self.db.cursor()
        try:
            cursor.execute("SELECT * FROM productos")  # Consultar todos los productos
            productos = cursor.fetchall()  # Obtener todos los registros
            return productos  # Devolver la lista de productos
        except Exception as e:
            return {"status": "error", "message": str(e)}