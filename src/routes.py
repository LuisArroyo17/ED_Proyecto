from flask import Blueprint, jsonify, request

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/optimize-route', methods=['POST'])
def optimize_route():
    data = request.get_json()
    # Aquí iría la lógica para optimizar la ruta usando el grafo
    optimized_route = {}  # Reemplaza con la lógica de optimización
    return jsonify(optimized_route)

