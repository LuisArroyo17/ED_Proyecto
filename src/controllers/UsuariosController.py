from flask import request
from models.ModelUsuario import ModelUsuario

class UsuariosController:
    def agregar_usuario(self):
        nombre = request.json.get('nombre')
        email = request.json.get('email')
        contrasena = request.json.get('contrasena')
        rol = request.json.get('rol', 'cliente')

        usuario = ModelUsuario().agregar_usuarioDB(nombre, email, contrasena, rol)
        return usuario

    def obtener_usuario(self, id):
        usuario = ModelUsuario().obtener_usuarioDB(id)
        return usuario

    def actualizar_usuario(self, id):
        nombre = request.json.get('nombre')
        email = request.json.get('email')
        rol = request.json.get('rol')

        usuario = ModelUsuario().actualizar_usuarioDB(id, nombre, email, rol)
        return usuario

    def eliminar_usuario(self, id):
        resultado = ModelUsuario().eliminar_usuarioDB(id)
        return resultado
