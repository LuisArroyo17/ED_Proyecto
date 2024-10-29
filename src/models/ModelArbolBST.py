class Nodo:
    def __init__(self, producto):
        self.id = producto["id"]
        self.nombre = producto["nombre"]
        self.precio = producto["precio"]
        self.categoria = producto["categoria"]
        self.descripcion = producto["descripcion"]
        self.stock = producto["stock"]
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar_por_atributo(self, arg, producto):
        if self.raiz is None:
            self.raiz = Nodo(producto)
        else:
            self.insertar_recursivo_por_atributo(arg, self.raiz, producto)
        return self.raiz

    def insertar_recursivo_por_atributo(self, arg , nodo_actual : Nodo, producto):
        if producto[arg] < nodo_actual.__getattribute__(arg):
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(producto)
            else:
                self.insertar_recursivo_por_atributo(arg, nodo_actual.izquierda, producto)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(producto)
            else:
                self.insertar_recursivo_por_atributo(arg, nodo_actual.derecha, producto)

    def inorden(self):
        productos = []
        self.inorden_recursivo(self.raiz, productos)
        return productos

    def inorden_recursivo(self, nodo_actual : Nodo, productos):
        if nodo_actual is not None:
            self.inorden_recursivo(nodo_actual.izquierda, productos)
            productos.append(
                {
                    "id": nodo_actual.id,
                    "nombre": nodo_actual.nombre,
                    "precio": nodo_actual.precio,
                    "categoria": nodo_actual.categoria,
                    "descripcion": nodo_actual.descripcion,
                    "stock": nodo_actual.stock 
                }
            )
            self.inorden_recursivo(nodo_actual.derecha, productos)
