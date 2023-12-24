# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_migrate import Migrate
from flaskr.config.database import db
from flaskr.config.routes import load_routes
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

    Migrate(app, db)

    load_routes(api)

    @app.cli.command('seed')
    def seed():
        Seeder.seed()

    @app.cli.command('unseed')
    def undo_seed():
        Seeder.unseed()

    return app
