from flask import Flask
from routes import productos_blueprint, pedidos_blueprint, usuarios_blueprint
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config
app.register_blueprint(pedidos_blueprint)
app.register_blueprint(productos_blueprint)
app.register_blueprint(usuarios_blueprint)

if __name__ == "__main__":
  app.run(debug=True)