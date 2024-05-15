from flask import Flask
from flask_restful import Api
from .db import init_db
from .app import Users, User


def create_app(config_object):
    app = Flask(__name__)
    api = Api(app)
    app.config.from_object(config_object)
    # init_db(app)

    api.add_resource(Users, '/users')
    api.add_resource(User, '/user', '/user/<string:cpf>')
    return app
