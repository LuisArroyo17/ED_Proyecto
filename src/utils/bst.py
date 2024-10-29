# utils/bst.py

class NodoProducto:
    def __init__(self, producto):
        self.producto = producto  # Producto almacenado en el nodo
        self.izquierda = None  # Hijo izquierdo
        self.derecha = None    # Hijo derecho
class ArbolProductoBST:
    def __init__(self):
        self.raiz = None

    def insertar(self, producto):
        """
        Insertar un producto en el árbol. 
        El criterio de ordenación puede ser el nombre o el ID del producto.
        """
        if not self.raiz:
            self.raiz = NodoProducto(producto)
        else:
            self._insertar_recursivo(self.raiz, producto)

    def _insertar_recursivo(self, nodo_actual, producto):
        if producto["nombre"] < nodo_actual.producto["nombre"]:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = NodoProducto(producto)
            else:
                self._insertar_recursivo(nodo_actual.izquierda, producto)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = NodoProducto(producto)
            else:
                self._insertar_recursivo(nodo_actual.derecha, producto)

    def buscar(self, nombre):
        """
        Buscar un producto por nombre en el árbol.
        """
        return self._buscar_recursivo(self.raiz, nombre)

    def _buscar_recursivo(self, nodo_actual, nombre):
        if nodo_actual is None:
            return None
        # print(f"Visitando nodo: {nodo_actual.producto['nombre']}")  # Debug
        if nombre == nodo_actual.producto["nombre"]:
            return nodo_actual.producto
        elif nombre < nodo_actual.producto["nombre"]:
            return self._buscar_recursivo(nodo_actual.izquierda, nombre)
        else:
            return self._buscar_recursivo(nodo_actual.derecha, nombre)