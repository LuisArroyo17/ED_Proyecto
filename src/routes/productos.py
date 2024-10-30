from flask import Blueprint, request, jsonify
from controllers.productos import ProductosController


productos_blueprint = Blueprint('producto', __name__)
productos_controller = ProductosController()

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

@productos_blueprint.route('/productos', methods=['GET'])
def obtener_productos():
    return ProductosController().obtener_productos()

# # Nuevo endpoint para listar productos con paginación y filtro por categoría
# @productos_blueprint.route('/productos', methods=['GET'])
# def listar_productos():
#     # Obtener parámetros de la URL para paginación y filtro
#     page = request.args.get('page', 1, type=int)      # Página actual
#     limit = request.args.get('limit', 10, type=int)    # Número de productos por página
#     categoria = request.args.get('categoria', None)    # Filtro opcional por categoría

#     # Llamar al método del controlador para obtener los productos
#     productos = ProductosController().listar_productos(page, limit, categoria)
    
#     # Retornar directamente la respuesta JSON
#     return productos  # Ya debe ser una respuesta JSON en el controlador

@productos_blueprint.route('/productos', methods=['GET'])
def listar_productos():
    # Obtener parámetros de la URL para paginación y filtro
    page = request.args.get('page', 1, type=int)      # Página actual
    limit = request.args.get('limit', 10, type=int)    # Número de productos por página
    categoria = request.args.get('categoria', None)    # Filtro opcional por categoría

    # Llamar al método del controlador para obtener los productos desde la memoria
    productos = productos_controller.listar_productos(page, limit, categoria)
    
    # Retornar directamente la respuesta JSON
    return jsonify(productos)

@productos_blueprint.route('/productos/buscar', methods=['GET'])
def buscar_producto_por_nombre():
    nombre = request.args.get('nombre')
    if not nombre:
        return {"message": "Nombre no proporcionado"}, 400
    return productos_controller.buscar_producto_por_nombre(nombre)