from flask import Blueprint
from controllers.ArbolController import ArbolBinarioController

arbol_blueprint = Blueprint('arbol', __name__)

@arbol_blueprint.route('/arbol/id', methods=['GET'])
def obtener_arbol():
    return ArbolBinarioController().cargar_arbol_por_id()

@arbol_blueprint.route('/arbol/nombre', methods=['GET'])
def obtener_arbol_por_nombre():
    return ArbolBinarioController().cargar_arbol_por_nombre()

@arbol_blueprint.route('/arbol/categoria', methods=['GET'])
def obtener_arbol_por_categoria():
    return ArbolBinarioController().cargar_arbol_por_categoria()