from flask import Flask
from flask_restful import Api

from .routes import load_routers

app = Flask(__name__)
api = Api(app)

load_routers(api)
