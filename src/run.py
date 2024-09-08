from flask import Flask
from routes import admin_blueprint
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config
app.register_blueprint(admin_blueprint)


if __name__ == "__main__":
  app.run(debug=True)