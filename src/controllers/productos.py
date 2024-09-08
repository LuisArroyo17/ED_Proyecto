class ProductosController:
    def __init__(self):
        self.productos = []

    def obtener_productos(self):
        return None

    def obtener_producto(self, id):
        for producto in self.productos:
            print(producto)
        return None

    def crear_producto(self):

        return None

    def eliminar_producto(self, nombre):
        producto = self.buscar_producto(nombre)
        if producto:
            self.productos.remove(producto)
            return True
        return False

    def actualizar_producto(self, id):
        producto = self.obtener_producto(id)
        return False