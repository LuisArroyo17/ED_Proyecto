from flask import Blueprint
from controllers.admin import AdminController


admin_blueprint = Blueprint('admin', __name__)

@admin_blueprint.route('/admin/register', methods=['POST'])
def insertar_admin():
    return AdminController().crear_admin()

@admin_blueprint.route('/admin/login', methods=['POST'])
def login_admin():
    return AdminController().login()