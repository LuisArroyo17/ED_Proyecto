from flask import request
from models.productos import ModelProducto

class ProductosController:
    @staticmethod
    def obtener_productos():
        productos=ModelProducto().obtener_productos()
        return productos
    @staticmethod
    def obtener_producto(id):
        producto=ModelProducto().obtener_productoDB_ID(id)
        if producto.get("data"):
            return producto
        else:
            return { "error": "Producto no encontrado." }
    
    @staticmethod
    def agregar_producto():
        nombre = request.json.get('nombre')
        precio = request.json.get('precio')
        categoria = request.json.get('categoria')
        descripcion = request.json.get('descripcion')
        
        producto=ModelProducto().agregar_productoDB(nombre, precio, categoria, descripcion)
        return producto
    
    @staticmethod
    def eliminar_producto(id):
        producto=ModelProducto().eliminar_productoDB(id)
        if producto.get("message") == "Producto eliminado.":
            print (producto)
            return producto
        else:
            return { "error": "Producto no encontrado." }
        
    
    @staticmethod
    def actualizar_producto(id):
        print(id)
        nombre = request.json.get('nombre')
        precio = request.json.get('precio')
        categoria = request.json.get('categoria')
        descripcion = request.json.get('descripcion')
        
        if not all([nombre, precio, categoria, descripcion]):
            return { "error": "Faltan datos para actualizar el producto." }, 400
        producto_modelo = ModelProducto()
        resultado= producto_modelo.actualizar_productoDB( id, nombre, precio, categoria, descripcion)
  
        return resultado