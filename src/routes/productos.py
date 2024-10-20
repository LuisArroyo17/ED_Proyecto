from flask import Blueprint
from controllers.productos import ProductosController


productos_blueprint = Blueprint('producto', __name__)

@productos_blueprint.route('/productos', methods=['POST']) 
def agregar_producto1():
    return ProductosController().agregar_producto()

@productos_blueprint.route('/productos/<int:id>', methods=['GET'])
def obtener_producto1(id):
    return ProductosController().obtener_producto(id)

@productos_blueprint.route('/productos/<int:id>', methods=['PUT'])
def actualizar_producto1(id):
    return ProductosController().actualizar_producto(id)

@productos_blueprint.route('/productos/<int:id>', methods=['DELETE'])
def eliminar_producto1(id):
    return ProductosController().eliminar_producto(id)
