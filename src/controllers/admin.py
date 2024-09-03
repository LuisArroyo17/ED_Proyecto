from models.admin import AdminModel
from flask import request

class AdminController:
    @staticmethod
    def crear_admin():
        username = request.json.get('Username: ')
        password = request.json.get('Password: ')
        first_name = request.json.get('First name: ')
        last_name = request.json.get('Last name: ')
        response= AdminModel().insertar_admin(username, password, first_name, last_name)
        if response:
            print('Admin creado con éxito')