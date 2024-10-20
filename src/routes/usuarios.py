from flask import Blueprint
from controllers.UsuariosController import UsuariosController


usuarios_blueprint = Blueprint('usuario', __name__)

@usuarios_blueprint.route('/usuarios', methods=['POST']) 
def agregar_usuario1():
    return UsuariosController().agregar_usuario()

@usuarios_blueprint.route('/usuarios/<int:id>', methods=['GET'])
def obtener_usuario1(id):
    return UsuariosController().obtener_usuario(id)

@usuarios_blueprint.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario1(id):
    return UsuariosController().actualizar_usuario(id)

@usuarios_blueprint.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario1(id):
    return UsuariosController().eliminar_usuario(id)
