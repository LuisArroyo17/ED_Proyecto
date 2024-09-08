from models.admin import AdminModel
from flask import request

class AdminController:
    @staticmethod
    def crear_admin():
        username = request.json.get('username')
        password = request.json.get('password')
        first_name = request.json.get('first_name')
        last_name = request.json.get('last_name')
        response= AdminModel().insertar_adminDB(username, password, first_name, last_name)
        if response:
            return response
        return { "error": "No se pudo registrar" }, 400
    @staticmethod
    def login():
        username = request.json.get('username')
        password = request.json.get('password')
        response = AdminModel().loginDB(username, password)
        if response:
            return response
        return { "error": "No se pudo loguear" }, 400