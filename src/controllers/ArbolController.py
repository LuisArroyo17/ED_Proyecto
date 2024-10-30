from flask import request
from models.ModelProducto import ModelProducto
from models.ModelArbolBST import ArbolBinario

class ArbolBinarioController:
    def cargar_arbol_por_id(self):
        arbol = ArbolBinario()
        resultado, status = ModelProducto().obtener_todos_productosDB()

        if status == 200:
            productos = resultado["data"]
        
            for prod in productos:
                arbol.insertar_por_atributo("id", prod)
            return arbol.inorden()
        else:
            return resultado, status
    
    def cargar_arbol_por_nombre(self):
        arbol = ArbolBinario()
        resultado, status = ModelProducto().obtener_todos_productosDB()

        if status == 200:
            productos = resultado["data"]
        
            for prod in productos:
                arbol.insertar_por_atributo("nombre", prod)
            return arbol.inorden()
        else:
            return resultado, status
    
    def cargar_arbol_por_categoria(self):
        arbol = ArbolBinario()
        resultado, status = ModelProducto().obtener_todos_productosDB()

        if status == 200:
            productos = resultado["data"]
        
            for prod in productos:
                arbol.insertar_por_atributo("categoria", prod)
            return arbol.inorden()
        else:
            return resultado, status