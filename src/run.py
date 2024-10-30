import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask
from routes import productos_blueprint, pedidos_blueprint, usuarios_blueprint, carritos_blueprint
from flask_cors import CORS
from config import Config

app = Flask(__name__)
CORS(app)
app.config
app.register_blueprint(pedidos_blueprint)
app.register_blueprint(productos_blueprint)
app.register_blueprint(usuarios_blueprint)
app.register_blueprint(carritos_blueprint)

if __name__ == "__main__":
  app.run(debug=True)

@app.route('/')
def home():
  return "Servidor funcionando correctamente"