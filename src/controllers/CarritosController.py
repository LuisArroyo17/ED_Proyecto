# Define el nodo de la lista doblemente enlazada
from flask import jsonify, request
from models.ModelCarrito import ModelCarrito

class NodoDoble:
    def __init__(self, producto):
        self.producto = producto
        self.siguiente = None
        self.anterior = None

# Define la lista doblemente enlazada
class ListaEnlazadaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar(self, producto):
        nuevo_nodo = NodoDoble(producto)
        if not self.cabeza:
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def eliminar(self, producto_id):
        nodo_actual = self.cabeza
        while nodo_actual:
            if nodo_actual.producto['id'] == producto_id:
                if nodo_actual.anterior:
                    nodo_actual.anterior.siguiente = nodo_actual.siguiente
                else:
                    self.cabeza = nodo_actual.siguiente
                if nodo_actual.siguiente:
                    nodo_actual.siguiente.anterior = nodo_actual.anterior
                else:
                    self.cola = nodo_actual.anterior
                    
                   
                return {"message": f"Producto con ID {producto_id} eliminado del carrito"}
            nodo_actual = nodo_actual.siguiente
        return {"message": f"Producto con ID {producto_id} no encontrado en el carrito"}

    def obtener_productos(self):
        productos = []
        nodo_actual = self.cabeza
        while nodo_actual:
            productos.append(nodo_actual.producto)
            nodo_actual = nodo_actual.siguiente
        return productos

# Variable global para el carrito temporal
carrito_temporal_global = ListaEnlazadaDoble()

# Controlador para manejar el carrito
class CarritosController:
    
    def __init__(self):
        # Usa la lista doblemente enlazada para el carrito temporal
        self.carrito_temporal = carrito_temporal_global
    """  
    def agregar_carrito(self):
        usuario_id = request.json.get('usuario_id')
        producto_id = request.json.get('producto_id')
        cantidad = request.json.get('cantidad')
    
        # Crear una instancia de ModelCarrito
        model_carrito = ModelCarrito()
        
        # Llamar al método de instancia
        carrito = model_carrito.agregar_carritoDB(usuario_id, producto_id, cantidad)
        return carrito
    """
    def traer_productos(self):
        # Crear una instancia de ModelCarrito
        model_carrito = ModelCarrito()
        
        productos = model_carrito.obtener_productosDB()
        return jsonify(productos)
    
    def añadir_carrito_temporal(self):
        producto_id = request.json.get('producto_id')
        cantidad = request.json.get('cantidad')

        model_carrito = ModelCarrito()
        productos = model_carrito.obtener_productosDB()
    
        # Buscar el producto en la base de datos
        producto_seleccionado = next((prod for prod in productos if prod['id'] == producto_id), None)
    
        if producto_seleccionado:
            # Hacer una copia del producto para no modificar el original
            producto_copia = producto_seleccionado.copy()
            producto_copia['cantidad'] = cantidad  # Agregar cantidad al producto seleccionado
            self.carrito_temporal.agregar(producto_copia)
            return {"message": "Producto agregado al carrito temporal", "carrito": self.carrito_temporal.obtener_productos()}
        else:
            return {"message": "Producto no encontrado", "carrito": self.carrito_temporal.obtener_productos()}

    def eliminar_producto_temporal(self):
        producto_id = request.json.get('producto_id')
        mensaje = self.carrito_temporal.eliminar(producto_id)
        return mensaje
    
    def obtener_carrito_temporal(self):
        return jsonify(self.carrito_temporal.obtener_productos())
    
    def agregar_productos_a_db(self, usuario_id):
        productos = self.carrito_temporal.obtener_productos()
        model_carrito = ModelCarrito()

        resultados = []
        for producto in productos:
            producto_id = producto['id']
            cantidad = producto['cantidad']
            resultado = model_carrito.agregar_carritoDB(usuario_id, producto_id, cantidad)
            resultados.append(resultado)
            # Eliminar el producto de la lista temporal después de agregarlo a la base de datos
            self.carrito_temporal.eliminar(producto_id)
        return jsonify(resultados)
    
    def obtener_carrito(self, usuario_id):
        model_carrito = ModelCarrito()
        carrito = model_carrito.obtener_carritoDB(usuario_id)
        return jsonify(carrito)