from routes.pedidos import pedidos_blueprint
from routes.usuarios import usuarios_blueprint
from routes.productos import productos_blueprint
from routes.carritos import carritos_blueprint
from routes.envios import envios_blueprint  # Agrega el blueprint de envíos
from routes.arbol_bst import arbol_blueprint

def register_blueprints(app):
    app.register_blueprint(pedidos_blueprint)
    app.register_blueprint(usuarios_blueprint)
    app.register_blueprint(productos_blueprint)
    app.register_blueprint(envios_blueprint)  # Registra el blueprint de envíos
