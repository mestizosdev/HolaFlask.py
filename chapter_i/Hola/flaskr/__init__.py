# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Api
from flaskr.config.routes import load_routes


app = Flask(__name__)
api = Api(app)

load_routes(api)
