from flask import request
from models.productos import ModelProducto

class ProductosController:
    @staticmethod
    def obtener_productos(self):
        productos=ModelProducto().obtener_productos()
        return productos
    @staticmethod
    def obtener_producto(self, id):
        producto=ModelProducto().obtener_producto(id)
        return producto
    @staticmethod
    def agregar_producto():
        nombre = request.json.get('nombre')
        precio = request.json.get('precio')
        categoria = request.json.get('categoria')
        descripcion = request.json.get('descripcion')
        
        producto=ModelProducto().agregar_productoDB(nombre, precio, categoria, descripcion)
        return producto
    @staticmethod
    def eliminar_producto(self, nombre):
        producto = self.buscar_producto(nombre)
        if producto:
            self.productos.remove(producto)
            return True
        return False
    @staticmethod
    def actualizar_producto(self, id):
        producto = self.obtener_producto(id)
        return False