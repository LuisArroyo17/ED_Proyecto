from flask import Flask
from routes import productos_blueprint, pedidos_blueprint, usuarios_blueprint, envios_blueprint, arbol_blueprint
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config

# Registrar todos los blueprints
app.register_blueprint(pedidos_blueprint)
app.register_blueprint(productos_blueprint)
app.register_blueprint(usuarios_blueprint)
app.register_blueprint(envios_blueprint)  # Registrar el blueprint de envíos
app.register_blueprint(arbol_blueprint)

if __name__ == "__main__":
  app.run(debug=True)