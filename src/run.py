import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask
from routes import productos_blueprint, pedidos_blueprint, usuarios_blueprint, envios_blueprint
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config

# Registrar todos los blueprints
app.register_blueprint(pedidos_blueprint)
app.register_blueprint(productos_blueprint)
app.register_blueprint(usuarios_blueprint)
app.register_blueprint(envios_blueprint)  # Registrar el blueprint de envíos

if __name__ == "__main__":
    app.run(debug=True)
