from models.admin import AdminModel
from flask import request

class AdminController:
    @staticmethod
    def crear_admin():
        username = request.json.get('username: ')
        password = request.json.get('password:')
        first_name = request.json.get('first_name:')
        last_name = request.json.get('last_name:')
        response= AdminModel().insertar_admin(username, password, first_name, last_name)
        if response:
            print('Admin creado con éxito')