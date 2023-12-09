# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Api
from flaskr.config.database import db
from flaskr.config.logger import define_logger
from flaskr.config.routes import load_routes


app = Flask(__name__)
api = Api(app)
app.config.from_pyfile('config/config.cfg')
db.init_app(app)

load_routes(api)
define_logger()
