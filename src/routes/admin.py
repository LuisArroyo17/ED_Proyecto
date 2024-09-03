from flask import Blueprint

admin_blueprint = Blueprint('admin', __name__)

@admin_blueprint.route('/admin', methods=['POST'])
def insertar_admin():
    return 'Admin insertado'