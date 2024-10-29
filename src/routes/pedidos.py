from flask import Blueprint
from controllers.PedidosController import PedidosController


pedidos_blueprint = Blueprint('pedidos', __name__)

@pedidos_blueprint.route('/pedidos', methods=['POST']) 
def agregar_pedido1():
    return PedidosController().agregar_pedido()

@pedidos_blueprint.route('/pedidos/<int:id>', methods=['GET'])
def obtener_pedido1(id):
    return PedidosController().obtener_pedido(id)

@pedidos_blueprint.route('/pedidos/<int:id>', methods=['PUT'])
def actualizar_pedido1(id):
    return PedidosController().actualizar_pedido(id)

@pedidos_blueprint.route('/pedidos/<int:id>', methods=['DELETE'])
def eliminar_pedido1(id):
    return PedidosController().eliminar_pedido(id)
