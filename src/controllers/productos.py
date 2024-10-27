# controllers/productos.py
from flask import request, jsonify
from models.ModelProducto import ModelProducto
from models.productos import Producto
from decimal import Decimal
from utils.bst import ArbolProductoBST  # Importa el BST

class ProductosController:
    def __init__(self):
        # Estructuras en memoria para los productos
        self.productos_lista = []      # Lista para iterar sobre los productos
        self.productos_dict = {}       # Diccionario para búsquedas rápidas por ID
        self.arbol_productos = ArbolProductoBST()  # Instancia del árbol de productos
        # Cargar productos desde la base de datos al iniciar
        self.cargar_productos_en_memoria()

    def cargar_productos_en_memoria(self):
        """
        Cargar todos los productos de la base de datos en las estructuras en memoria.
        """
        
        # Obtener todos los productos de la base de datos
        productos_db = ModelProducto().obtener_productos()

        
        # Limpiar estructuras en memoria
        self.productos_lista.clear()
        self.productos_dict.clear()
        self.arbol_productos = ArbolProductoBST()  # Reiniciar el árbol
        # Llenar estructuras en memoria
        for producto_data in productos_db:
            # Convertir los datos del producto en un diccionario o instancia
            producto = {
                "id": producto_data["id"],
                "nombre": producto_data["nombre"],
                "precio": float(producto_data["precio"]),
                "categoria": producto_data["categoria"],
                "descripcion": producto_data["descripcion"],
                "stock": producto_data["stock"]
            }
            # Agregar el producto a las estructuras en memoria
            self.productos_lista.append(producto)
            self.productos_dict[producto["id"]] = producto
            self.arbol_productos.insertar(producto)  # Insertar en el árbol BST
    # Métodos CRUD utilizando tanto la base de datos como las estructuras en memoria
    def buscar_producto_por_nombre(self, nombre):
        """
        Buscar un producto en el BST por su nombre.
        """
        producto = self.arbol_productos.buscar(nombre)
        if producto:
            return {"data": producto}, 200
        else:
            return {"message": "Producto no encontrado"}, 404
    def agregar_producto(self):
        nombre = request.json.get('nombre')
        precio = request.json.get('precio')
        categoria = request.json.get('categoria')
        descripcion = request.json.get('descripcion')
        stock = request.json.get('stock')

        # Agregar producto a la base de datos
        resultado = ModelProducto().agregar_productoDB(nombre, precio, categoria, descripcion, stock)

        # Si el producto se agrega correctamente en la base de datos, también lo añadimos en memoria
        if resultado[1] == 201:  # Verificar si el estado es éxito (201)
            nuevo_producto = {
                "id": resultado[0]["last_row_id"],  # Obtener el ID generado
                "nombre": nombre,
                "precio": float(precio),
                "categoria": categoria,
                "descripcion": descripcion,
                "stock": stock
            }
            self.productos_lista.append(nuevo_producto)
            self.productos_dict[nuevo_producto["id"]] = nuevo_producto

        return resultado

    def obtener_producto(self, id):
        # Buscar en el diccionario en memoria para acceso rápido
        producto = self.productos_dict.get(id)
        if producto:
            return {"data": producto}, 200
        return {"message": "Producto no encontrado"}, 404

    def actualizar_producto(self, id):
        nombre = request.json.get('nombre')
        precio = request.json.get('precio')
        categoria = request.json.get('categoria')
        descripcion = request.json.get('descripcion')
        stock = request.json.get('stock')

        # Actualizar en la base de datos
        resultado = ModelProducto().actualizar_productoDB(id, nombre, precio, categoria, descripcion, stock)

        # Si la actualización fue exitosa, actualizamos también en memoria
        if resultado[1] == 200:
            if id in self.productos_dict:
                self.productos_dict[id].update({
                    "nombre": nombre,
                    "precio": float(precio),
                    "categoria": categoria,
                    "descripcion": descripcion,
                    "stock": stock
                })
                # Actualizar también en la lista
                for producto in self.productos_lista:
                    if producto["id"] == id:
                        producto.update(self.productos_dict[id])

        return resultado

    def eliminar_producto(self, id):
        # Eliminar de la base de datos
        resultado = ModelProducto().eliminar_productoDB(id)

        # Si la eliminación fue exitosa, también eliminamos en memoria
        if resultado[1] == 200:
            # Eliminar en el diccionario
            if id in self.productos_dict:
                del self.productos_dict[id]
            # Eliminar en la lista
            self.productos_lista = [p for p in self.productos_lista if p["id"] != id]

        return resultado

    def listar_productos(self, page=1, limit=10, categoria=None):
    # Calcula el offset en función de la página y el límite
        offset = (page - 1) * limit
        productos = ModelProducto().obtener_productos(offset=offset, limit=limit, categoria=categoria)
        return {"data": productos}