from routes.pedidos import pedidos_blueprint
from routes.usuarios import usuarios_blueprint
from routes.productos import productos_blueprint
from routes.envios import envios_blueprint  # Agrega el blueprint de envíos

def register_blueprints(app):
    app.register_blueprint(pedidos_blueprint)
    app.register_blueprint(usuarios_blueprint)
    app.register_blueprint(productos_blueprint)
    app.register_blueprint(envios_blueprint)  # Registra el blueprint de envíos
