from flask import Flask
from db import db

from controllers.native.mouse import app as mouse_controller

def create_app():
  app = Flask(__name__)

  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'

  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  app.register_blueprint(mouse_controller)

  db.init_app(app)

  with app.app_context():
      db.create_all()

  return app

if __name__ == '__main__':
  app = create_app()
  app.run(debug=True)