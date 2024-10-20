from flask import request
from models.productos import ModelProducto

class ProductosController:
    def agregar_producto(self):
        nombre = request.json.get('nombre')
        precio = request.json.get('precio')
        categoria = request.json.get('categoria')
        descripcion = request.json.get('descripcion')
        stock = request.json.get('stock')

        producto = ModelProducto().agregar_productoDB(nombre, precio, categoria, descripcion, stock)
        return producto

    def obtener_producto(self, id):
        producto = ModelProducto().obtener_productoDB(id)
        return producto

    def actualizar_producto(self, id):
        nombre = request.json.get('nombre')
        precio = request.json.get('precio')
        categoria = request.json.get('categoria')
        descripcion = request.json.get('descripcion')
        stock = request.json.get('stock')

        producto = ModelProducto().actualizar_productoDB(id, nombre, precio, categoria, descripcion, stock)
        return producto

    def eliminar_producto(self, id):
        resultado = ModelProducto().eliminar_productoDB(id)
        return resultado
