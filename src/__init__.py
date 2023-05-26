from flask import Flask
from flask_restful import Api
from .endpoints import initialize_endpoints

from .models.models import db

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mercado.db'

    db.init_app(app)

    api = Api(app, prefix="/api")
    initialize_endpoints(api)

    return app