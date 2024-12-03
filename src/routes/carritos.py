from flask import Blueprint, request
from controllers.CarritosController import CarritosController

# Crear un blueprint para el carrito
carritos_blueprint = Blueprint('carrito', __name__)

# Ruta para traer todos los productos de la BD
@carritos_blueprint.route('/productos/traer/todos', methods=['GET'])
def traer_todo():
    return CarritosController().traer_productos()

# Ruta para agregar un producto de manera temporal al carrito (insertarlo en una lista doble enlazada)
@carritos_blueprint.route('/carrito/temporal/agregar', methods=['POST'])
def añadir_carrito_temporal():
    return CarritosController().añadir_carrito_temporal()

# Ruta para eliminar un producto de la lista doble enlazada
@carritos_blueprint.route('/carrito/temporal/eliminar', methods=['DELETE'])
def eliminar_producto_temporal():
    return CarritosController().eliminar_producto_temporal()

# Ruta para poder ver todos los productos del carrito de compras temporal
@carritos_blueprint.route('/carrito/temporal/ver', methods=['GET'])
def obtener_carrito_temporal():
    return CarritosController().obtener_carrito_temporal()

# Ruta para vaciar el carrito temporal
@carritos_blueprint.route('/carrito/temporal/vaciar', methods=['DELETE'])
def vaciar_carrito_temporal():
    return CarritosController().vaciar_carrito_temporal()

# Ruta para subir de manera oficial los porductos del carrito de compras
@carritos_blueprint.route('/carrito/oficial', methods=['POST'])
def agregar_producto_carrito_bd():
    usuario_id = request.json.get('usuario_id')
    return CarritosController().agregar_productos_a_db(usuario_id)

#carga el carrito de la DB
@carritos_blueprint.route('/cargarCarrito', methods=['POST'])
def obtenercarrito_bd():
    usuario_id = request.json.get('usuario_id')
    return CarritosController().obtener_carrito(usuario_id)
