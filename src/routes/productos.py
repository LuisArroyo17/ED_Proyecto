from flask import Blueprint
from controllers.productos import ProductosController


productos_blueprint = Blueprint('producto', __name__)

@productos_blueprint.route('/obtenerproductos', methods=['GET']) #Listo
def obtener_productos1():
    return ProductosController().obtener_productos()

@productos_blueprint.route('/Buscarproducto/<int:id>', methods=['GET']) #Listo
def buscar_producto(id):
    return ProductosController().obtener_producto(id)

@productos_blueprint.route('/productos', methods=['POST']) #Listo
def agregar_producto1():
    return ProductosController().agregar_producto()

@productos_blueprint.route('/producto/<int:id>', methods=['PUT']) #Listo
def actualizar_producto1(id):
    return ProductosController().actualizar_producto(id)

@productos_blueprint.route('/productos/<int:id>', methods=['DELETE']) #Listo
def eliminar_producto1(id):
    return ProductosController().eliminar_producto(id)
