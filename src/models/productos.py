# models/producto.py

class Producto:
    def __init__(self, id, nombre, precio, categoria, descripcion, stock):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.descripcion = descripcion
        self.stock = stock

    def __repr__(self):
        return f"{self.nombre} - {self.categoria} - ${self.precio}"
    
