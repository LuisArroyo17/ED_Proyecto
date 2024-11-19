from flask import request
from models.ModelUsuario import ModelUsuario

class UsuariosController:
    def agregar_usuario(self):
        try:
            # Obtener datos del request
            nombre = request.json.get('nombre')
            email = request.json.get('email')
            contrasena = request.json.get('contrasena')
            rol = request.json.get('rol', 'cliente')  # Por defecto, el rol será 'cliente'

            if not all([nombre, email, contrasena]):
                return {"message": "Todos los campos son obligatorios"}, 400

            # Verificar si el email ya está registrado
            usuario_existente = ModelUsuario().obtener_usuario_por_emailDB(email)
            if usuario_existente[1] == 200:  # Si el email ya existe
                return {"message": "El email ya está registrado"}, 400

            # Llamar al modelo para agregar el usuario
            return ModelUsuario().agregar_usuarioDB(nombre, email, contrasena, rol)
        except Exception as e:
            return {"status": "error", "message": str(e)}, 500

    def login(self):
        try:
            email = request.json.get('email')
            contrasena = request.json.get('contrasena')

            if not email or not contrasena:
                return {"message": "Email y contraseña son obligatorios"}, 400

            # Obtener el usuario por email
            result, status_code = ModelUsuario().obtener_usuario_por_emailDB(email)
            if status_code != 200:
                return result, status_code

            usuario = result['data']

            # Verificar la contraseña
            if usuario['contrasena'] != contrasena:
                return {"message": "Credenciales inválidas"}, 401

            # Login exitoso
            return {
                "message": f"Bienvenido {usuario['nombre']}",
                "usuario": {
                    "id": usuario['id'],
                    "nombre": usuario['nombre'],
                    "email": usuario['email'],
                    "rol": usuario['rol']
                }
            }, 200
        except Exception as e:
            return {"status": "error", "message": str(e)}, 500

    def obtener_usuario(self, id):
        try:
            return ModelUsuario().obtener_usuarioDB(id)
        except Exception as e:
            return {"status": "error", "message": str(e)}, 500

    def actualizar_usuario(self, id):
        try:
            nombre = request.json.get('nombre')
            email = request.json.get('email')
            rol = request.json.get('rol')

            if not all([nombre, email, rol]):
                return {"message": "Todos los campos son obligatorios"}, 400

            return ModelUsuario().actualizar_usuarioDB(id, nombre, email, rol)
        except Exception as e:
            return {"status": "error", "message": str(e)}, 500

    def eliminar_usuario(self, id):
        try:
            return ModelUsuario().eliminar_usuarioDB(id)
        except Exception as e:
            return {"status": "error", "message": str(e)}, 500
