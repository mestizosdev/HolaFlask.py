# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_migrate import Migrate
from flaskr.config.database import db
from flaskr.config.logger import define_logger
from flaskr.config.routes import load_routes
from flaskr.seeder import Seeder
from flaskr.config.models import *  # noqa


app = Flask(__name__)
CORS(app)
api = Api(app)
app.config.from_pyfile('config/config.cfg')
db.init_app(app)

migrate = Migrate(app, db)

load_routes(api)
define_logger()


@app.cli.command('seed')
def seed():
    Seeder.seed()


@app.cli.command('unseed')
def undo_seed():
    Seeder.unseed()
