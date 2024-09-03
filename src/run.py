from flask import Flask
from routes import admin_blueprint


app = Flask(__name__)
app.config
app.register_blueprint(admin_blueprint)


if __name__ == "__main__":
  app.run(debug=True)