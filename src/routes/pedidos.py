from flask import Blueprint, request, jsonify
from controllers.PedidosController import PedidosController

# Instancia de Blueprint y del controlador de pedidos
pedidos_blueprint = Blueprint('pedidos', __name__)
pedidos_controller = PedidosController()

# Ruta para agregar un pedido (POST)
@pedidos_blueprint.route('/pedidos', methods=['POST']) 
def agregar_pedido():
    return pedidos_controller.agregar_pedido()

# Ruta para obtener el siguiente pedido en la cola sin procesarlo (GET)
@pedidos_blueprint.route('/pedidos/ver_siguiente', methods=['GET'])
def ver_siguiente_pedido():
    return pedidos_controller.ver_siguiente_pedido()

# Ruta para procesar el siguiente pedido en la cola (POST)
@pedidos_blueprint.route('/pedidos/procesar', methods=['POST'])
def procesar_pedido():
    return pedidos_controller.procesar_pedido()

# Ruta para cancelar un pedido específico (POST)
@pedidos_blueprint.route('/pedidos/cancelar/<int:pedido_id>', methods=['POST'])
def cancelar_pedido(pedido_id):
    return pedidos_controller.cancelar_pedido(pedido_id)

# Ruta para actualizar el estado de un pedido específico (PUT)
@pedidos_blueprint.route('/pedidos/actualizar_estado/<int:pedido_id>', methods=['PUT'])
def actualizar_estado_pedido(pedido_id):
    data = request.get_json()
    nuevo_estado = data.get('estado', 'pendiente')
    return pedidos_controller.actualizar_estado_pedido(pedido_id, nuevo_estado)

# Ruta para obtener todos los pedidos en la cola (GET)
@pedidos_blueprint.route('/pedidos', methods=['GET'])
def mostrar_pedidos():
    return pedidos_controller.mostrar_pedidos()

@pedidos_blueprint.route('/pedidos/todos', methods=['GET'])
def mostrar_todos_pedidos():
    return pedidos_controller.mostrar_todos_pedidos()
#*****************Interacción directa con la DB*****************

# Ruta para obtener un pedido específico de la base de datos (GET)
@pedidos_blueprint.route('/pedidos/<int:id>', methods=['GET'])
def obtener_pedido(id):
    return pedidos_controller.obtener_pedido(id)

# Ruta para eliminar un pedido específico de la base de datos (DELETE)
@pedidos_blueprint.route('/pedidos/<int:id>', methods=['DELETE'])
def eliminar_pedido(id):
    return pedidos_controller.eliminar_pedido(id)

