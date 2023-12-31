# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_migrate import Migrate
from flaskr.config.database import db
from flaskr.config.jwt import jwt
from flaskr.config.routes import load_routes
from flaskr.config.logger import define_logger
from flaskr.seeder import Seeder
from flaskr.config.models import *  # noqa


def create_app(env='development'):
    app = Flask(__name__)
    CORS(app)
    api = Api(app)

    if env == 'development':
        app.config.from_pyfile('config/config.cfg')
    elif env == 'test':
        app.config.from_pyfile('config/config.test.cfg')

    db.init_app(app)
    jwt.init_app(app)

    Migrate(app, db)

    load_routes(api)
    define_logger(app)

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_data):
        return {'message': 'The token has expired'}, 401

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return {'message': 'Signature verification failed'}, 401

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return {'message': 'Request does not contain an access token'}, 401

    @app.cli.command('seed')
    def seed():
        Seeder.seed()

    @app.cli.command('unseed')
    def undo_seed():
        Seeder.unseed()

    return app
