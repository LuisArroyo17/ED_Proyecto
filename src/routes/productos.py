from flask import Blueprint
from controllers.productos import ProductosController


productos_blueprint = Blueprint('admin', __name__)

@productos_blueprint.route('/productos', methods=['GET'])
def insertar_admin():
    return ProductosController().obtener_productos()

@productos_blueprint.route('/productos/<int:id>', methods=['GET'])
def insertar_admin():
    return ProductosController().obtener_producto(id)

@productos_blueprint.route('/productos', methods=['POST'])
def insertar_admin():
    return ProductosController().crear_producto()

@productos_blueprint.route('/productos/<int:id>', methods=['PUT'])
def insertar_admin():
    return ProductosController().actualizar_producto(id)

@productos_blueprint.route('/productos/<int:id>', methods=['DELETE'])
def insertar_admin():
    return ProductosController().eliminar_producto(id)
